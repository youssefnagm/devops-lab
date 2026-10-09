# devops-lab

Practice repo for learning Linux, Git, Docker, and basic networking.

## check_sites.py
A small Python script that checks whether websites are up.
Run it with: python3 check_sites.py

## Run with Docker
docker build -t site-checker .
docker run --rm site-checker

## CI
A GitHub Actions workflow runs the script on every push.

## What I learned
- Reading HTTP status codes (200, 301, 302)
- DNS errors vs HTTP errors
- Packaging a script into a Docker image
- Running a script automatically with GitHub Actions 
