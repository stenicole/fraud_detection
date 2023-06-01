docker build --no-cache -f Dockerfile_fastapi -t fastapi_snicole:latest .
docker build --no-cache -f Dockerfile_authent -t authent:latest .
docker build --no-cache -f Dockerfile_authoriz -t authoriz:latest .
docker build --no-cache -f Dockerfile_content -t content:latest .
