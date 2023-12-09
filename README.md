
# IM 2024 Project

A small project that showcases Python, REST API (FastAPI), Docker, Pandas and SQL (Postgres) in a microservice architecture.


## Installation

- Install Docker Desktop or similar container tool for local development.
- Execute the following commands in the root directory of the project:

```bash
  docker-compose up -d
```

- If you are observing 502 Bad Gateway in NGINX you could try to run it on the same network before executing the command above:

```bash
  docker run --name nginx -d -v /root/nginx/conf:/etc/nginx/conf.d --net=host nginx
```


To reach the Swagger UI, open the following links:
- http://localhost:8080/api/v1/movies/docs for movie service docs
- http://localhost:8080/api/v1/casts/docs for cast service docs
