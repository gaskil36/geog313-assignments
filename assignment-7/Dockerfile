FROM continuumio/miniconda3:24.7.1-0

COPY environment.yml .
RUN conda env create -f environment.yml

# Activate the Conda environment
RUN echo "conda activate assignment-7" >> ~/.bashrc
ENV PATH /opt/conda/envs/assignment-7/bin:$PATH

# Create a non-root user and switch to that user
RUN useradd -m gisuser
USER gisuser

WORKDIR /home/gisuser

# Expose the JupyterLab port
EXPOSE 8888

# Expose the Dask Port
EXPOSE 8787

# Start JupyterLab
CMD ["jupyter", "lab", "--ip=0.0.0.0"]