## Dockerization- main codes:

- docker build -t REGION-docker.pkg.dev/${PROJECT_ID}/hello-repo/hello-app:v1 .
( DONT FORGET THE DOT to imply copy from current dir)

- docker push REGION-docker.pkg.dev/${PROJECT_ID}/hello-repo/hello-app:v1

- docker build -t  docker.io/bishnupoudel/flaskapp:cloudninefirst .

- docker login -u bishnupoudel -p <password>
- docker run -it  bishnupoudel/flaskapp:cloudninefirst

## For ECR aws:
- create a registry with label and copy the codes 