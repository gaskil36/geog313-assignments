## Assignment 4: Creating a Dockerized Conda Environment

### How to run this container
1. Pull this git repository to your local machine  
``` git pull https://github.com/gaskil36/geog313-assignments/tree/main```
2. Navigate to the following directory ```/geog313-assignments/a4```
3. Ensure the directory contains the following files:  
```Assignment4.ipynb``` 
```Dockerfile```  
```README.MD```  
```environment.yml```  
4. Build the Docker container:  
```docker build -t assignment4 .```  
5. Run the Docker container, ensuring port 8888 is open and the current local directory is mounted to the container (in order to access the Jupyter notebook outside of the container):  
```docker run -it -p 8888:8888 -v $(pwd):/home/assignment assignment4```  
6. The Docker container is now running. Click the link to open Jupyter Lab and run the following file:  
```Assignment4.ipynb```