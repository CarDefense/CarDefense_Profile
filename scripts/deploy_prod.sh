docker build -t tayh/api_profile:prod .
docker login -u "$DOCKER_USERNAME" -p "$DOCKER_PASSWORD"
docker push tayh/api_profile:prod