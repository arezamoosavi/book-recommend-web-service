# Book Recommend System

This recommender web service is build with flask, that for posted book will suggest similar books. The dataset is from goodreads.

## Installation

Starting app:

```bash
docker-compose up --build
```
Shutting it down:

```bash
docker-compose down -v
```

## Usage

First get token:
post request with "username" and "password"
```http
http://0.0.0.0:8000/register
```
copy the token after registration.
Add "api-token" with value of token in header.
Get request to get recommendation:
```http
http://0.0.0.0:8000/recommend/the stepford wives/20
```
To get serach history:
Get request:
```http
http://0.0.0.0:8000/
```

## Results
recommended books:
![alt text](https://github.com/arezamoosavi/book-recommend-web-service/blob/master/result.jpeg?raw=true)

## Tools
ML: Pandas, Sklearn

Tasks: Celery, rabbitmq, redis

Web: flask, cassandra, nginx, gunicorn

Build: docker, docker-compose

## Medium
### [part1](https://medium.com/@sdamoosavi/book-recommender-web-service-ml-e79119535258)
### [part2](https://medium.com/@sdamoosavi/book-recommender-web-service-cassandra-4a359917d713)
### [part3](https://medium.com/@sdamoosavi/book-recommender-web-service-flask-and-celery-18c8245a257e)
