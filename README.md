# Unified-Assignments1-1269-bwilliams
# Library Management System

![CI](https://github.com/brandonwilliams-tech/Unified-Assignments1-1269-bwilliams/actions/workflows/ci.yaml/badge.svg)

A FastAPI app with two endpoints: `/books` and `/health`.

## Build
```
docker build -t library-api:v1 .
```

## Run
```
docker run -d -p 8080:8080 library-api:v1
curl http://localhost:8080/health
curl http://localhost:8080/books
```

## Publish
ECR:
```
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 808949116514.dkr.ecr.us-east-1.amazonaws.com
docker tag library-api:v1 808949116514.dkr.ecr.us-east-1.amazonaws.com/library-api:v1
docker push 808949116514.dkr.ecr.us-east-1.amazonaws.com/library-api:v1
```
Docker Hub:
```
docker login -u brandon8721
docker tag library-api:v1 brandon8721/library-api:v1
docker push brandon8721/library-api:v1
```

## Team
| Member | Tasks |
|---|---|
|Matthew Juskovic | |
| Brandon Williams | |
