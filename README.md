
# IM 2024 Project

A small project that showcases Python, REST API (FastAPI), Docker, Pandas and SQL (Postgres) in a microservice architecture.


## Installation

Install Docker Desktop or similar container tool for local development.
Execute the following commands in the root directory of the project:

```bash
  docker build -t myimage .
  docker run -d --name mycontainer -p 80:80 myimage
```
    
To reach the Swagger UI, open the following link:
http://127.0.0.1/docs
