# ML_app_deployment_using_docker
In this repo I have added simple ML app train and validate the model using flask app. Use docker to run the app in container env.

This project is divided into below steps:
- Train the ML model
- Save and Export the model
- Create flask app with Swagger api
- Import trained model and add code for prediction
- build the docker image
- run the docker image
- stop the container


**Docker commands**

- First build the docker image

```
docker build -t ml_app_docker .
```

- Run the docker container

```
docker container run -p 5000:5000 ml_app_docker
```

- Stop the docker container
  - first get container-id
  ```
  docker ps -a
  ```
  - stop the container or kill it
  ```
  docker container stop <container-id>
  ```
