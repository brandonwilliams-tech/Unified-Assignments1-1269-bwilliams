# Unified-Assignments1-1269-bwilliams
# Library Management System

![Unit & API tests](https://github.com/brandonwilliams-tech/Unified-Assignments1-1269-bwilliams/actions/workflows/unit-tests.yml/badge.svg)
![SAST](https://github.com/brandonwilliams-tech/Unified-Assignments1-1269-bwilliams/actions/workflows/sast.yml/badge.svg)
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
| Brandon Williams | • Created the repo and the main branch ruleset (PR required, 1 approval, required checks, no direct pushes, force-push block, Copilot review)<br>• Set up pre-commit with Black, Flake8 and Bandit, and tested it (PR #2)<br>• Built the original CI workflow: Python 3.12+ venv, requirements.txt, pytest, and the API tests for /books and /health<br>• Added Semgrep SAST and OWASP Dependency-Check (fails on CVSS 7+)<br>• Wrote the Dockerfile (multi-stage, non-root user) and the app<br>• Opened PR #5 (Semgrep blocking)<br>• Added the AWS and Docker Hub secrets and ran the AWS Academy lab for the push<br>• Wrote the push step code<br>• Added docker-scan to the ruleset as a required check<br>• Resolved the duplicate PR #10 conflict<br>• Approved and merged PRs<br>• Task 4 credentials write-up (with Matthew) |
| Matthew Juskovic | • Added the docker-scan job (Trivy image scan) to the CI workflow and fixed the broken setup-trivy version<br>• Fixed the 4 HIGH vulnerabilities by removing pip and setuptools from the final image (Dockerfile change)<br>• Added the container run and /health and /books endpoint test steps to CI<br>• Added the ECR and Docker Hub push steps to the workflow (code from Brandon)<br>• Split unit tests and SAST into their own workflow files and updated the README badges<br>• Filled in the README team task list<br>• Reviewed, updated and merged PR #5<br>• Task 4 credentials write-up (with Brandon) |