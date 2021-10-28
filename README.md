# CityInsight

Python flask app to search city present in given endpoint.

---
## HOW TO RUN:

Prerequisite: 
- Python version 3.6+
  OR
- Docker Engine 

## Run Project without using Docker
- clone this repo to local machine
  - ```git clone https://github.com/apatils/CityInsight.git ```
- install required pip packages
  - ```pip install -r requirements.txt```
- run flask app using below command
  - ```python web_app.py``` 
- open browser with below URL
  - ```localhost:5050/```
---
## Run Project using Docker
- Make sure docker is installed on your local machine
  - ```docker build -t cityinsight .``` 
- After successfully docker build, verify if image is availble with name "cityinsight:latest" using below command
  - ```docker images```
- Finally run docker container with below command
  - ```docker run -dit -p 5050:5050 cityinsight```
- open browser with below URL
  - ```localhost:5050/``` 

---
## Run Directly from docker-hub
- 1 version is deployedon docker-hub, if you don't wish to build dockerfile and run directly can use this way
- ```docker run -dit -p 5050:5050 akashp/cityinsight:1.0.0-1```
- open browser with below URL
  - ```localhost:5050/```
---
 
## Contributor
- Akash Patil <patilakashsuresh@gmail.com>