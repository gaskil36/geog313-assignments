## Assignment 7: Using Dask-GeoPandas and Source Cooperative to analyze vector datasets. 

1. Clone this git repository to your local machine  
``` git pull https://github.com/gaskil36/geog313-assignments/tree/main/assignment-7```  
2. Ensure the directory contains the following files:  
```Dockerfile```  
```assignment-7.ipynb```
```environment.yml```  
```README.md``` 

### How to run this container  
1. Pull this Docker image from Docker Hub  
``` docker pull bengaskill12/assignment-7:latest```  
3. Build the docker container:  
```docker build -t assignment-7 .```  
4. Run the Docker container, ensuring port 8888 is open and the current local directory is mounted to the container (in order to access the Jupyter notebook outside of the container):  
```docker run -it -p 8888:8888 -p 8787:8787 -v $(pwd):/home/gisuser assignment-7```  
5. The Docker container is now running. Click the link to open Jupyter Lab and run the following file:  
```assignment7.ipynb```
