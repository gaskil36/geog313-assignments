import os
import dask_geopandas as dg
import geopandas as gpd
import requests 
import tqdm

def get_s3_keys(bucket_name, prefix, client):
    """
    This function returns all the S3 keys associated with a country_code
    from the Google Open Building Dataset on Source Cooperative. This function
    only lists the files in GeoParquet format.
    For more information about the dataset, visit 
    https://source.coop/repositories/cholmes/google-open-buildings/description/
    
    
    Inputs:
    --------
    country_code : string 
        A sting indicating the country of target. Country code is the Alpha-2 code based on ISO 3166 standard.
    client : boto3 client object 
        A s3 client returned by boto3.client
    
    
    Returns:
    --------
    keys: list
        List of all keys that match the country_code
    """

    keys = []    

    response = client.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
    for obj in response['Contents']:
        keys.append(obj['Key'])

    return keys  

def get_gdam_json(country_code, admin_level):


    url = f"https://geodata.ucdavis.edu/gadm/gadm4.1/json/gadm41_{country_code}_{admin_level}.json.zip"
    boundaries = gpd.read_file(url)
    boundaries = boundaries.rename(columns={f"NAME_{admin_level}": "Parish"})
    
    return boundaries
                  
def get_google_microsoft_bldgs(country_code, s3_client):

    bucket_name = 'vida'
    prefix = "google-microsoft-open-buildings/geoparquet/by_country/country_iso="
    country_prefix = f"{prefix}{country_code}"
    keys = get_s3_keys(bucket_name, country_prefix, s3_client)

    for key in keys:
        local_fname = f"./data/{key.split("/")[-1]}"
        if not os.path.exists(local_fname):
            print(f"File not found locally. Downloading from s3...")
            
            try:
                s3_client.download_file(Bucket = bucket_name,
                                        Key = key,
                                        Filename = f"./data/{key.split("/")[-1]}"
                                       )
                print("Download complete.")
            except:
                print("An error occurred. Download failed")
        else:
            print("File already exists locally. No download needed.")

    bldg_ddf = dg.read_parquet(f"./data/{country_code}*.parquet", gather_spatial_partitions=False)

    return bldg_ddf