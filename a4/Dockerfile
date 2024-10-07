FROM continuumio/miniconda3:24.7.1-0

# Copy environment.yml file 
COPY environment.yml .

# Create a Conda environment a-4env from environment.yml file
RUN conda env create -f environment.yml

# Activate the Conda environment
RUN echo "conda activate a4-env" >> ~/.bashrc
ENV PATH="$PATH:/opt/conda/envs/a4-env/bin"

# Create a non-root user and switch to that user
RUN useradd -m jupyteruser
USER jupyteruser

# Set the working directory to /home/jupyteruser
WORKDIR /home/assignment

# Expose the JupyterLab port
EXPOSE 8888

# Start JupyterLab
CMD ["jupyter", "lab", "--ip=0.0.0.0"]