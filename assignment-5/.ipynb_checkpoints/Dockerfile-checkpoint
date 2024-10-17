FROM continuumio/miniconda3:22.11.1

# Create a Conda environment with JupyterLab installed
RUN conda install numpy=1.23.1 jupyterlab=3.6.3 matplotlib=3.7.2
RUN conda install pystac-client --channel conda-forge

# Create a non-root user and switch to that user
RUN useradd -m jupyteruser
USER jupyteruser

WORKDIR /home/jupyteruser

# Expose the JupyterLab port
EXPOSE 8888

# Start JupyterLab
CMD ["jupyter", "lab", "--ip=0.0.0.0"]

