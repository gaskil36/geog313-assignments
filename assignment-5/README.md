## Assignment 5: Search for Satellite Imagery  

1. Clone this git repository to your local machine  
``` git pull https://github.com/gaskil36/geog313-assignments/tree/main/assignment-5```  
2. Ensure the directory contains the following files:  
```Dockerfile```  
```s2_query.ipynb``  
```README.md``` 

### How to run this container  
1. Pull this Docker image from Docker Hub  
``` docker pull bengaskill12/assignmentfive:latest```  
3. Build the docker container:  
```docker build -t assignmentfive .```  
4. Run the Docker container, ensuring port 8888 is open and the current local directory is mounted to the container (in order to access the Jupyter notebook outside of the container):  
```docker run -it -v $(pwd):/home/jupyteruser -p 8888:8888 assignmentfive```  
5. The Docker container is now running. Click the link to open Jupyter Lab and run the following file:  
```s2_query.ipynb```