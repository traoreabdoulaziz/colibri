# awslambda-fastapi
Deploy fastapi app

# How to use

## In local
- Create virtual env with *pipenv*
```
pipenv install -r requirements.txt
```
- Go to app directory and launch api
```
pipenv run uvicorn main:app --reload
```
- Then go to `localhost:8000/docs` to test api

## Development in container With docker
1. Build the app image
```sh
 docker-compose build
```
2. For running application type:
```sh
 docker-compose up
```
3. Go to http://localhost:8080/docs to see API documentation in your browser


## Deployment in container Heroku

1. Log in to your Heroku account

```sh
heroku login
```
2. You must sign into Container Registry

```sh
 heroku container:login
```
3. Build the Dockerfile in the current directory and push the Docker image.

```sh
 heroku container:push web --app <APP-NAME>
```
4 .Release the newly pushed images to deploy your app.

```sh
 heroku container:release web --app <APP-NAME>
```

## Test the application with Postman

1. Create user 

Method: Post
URL(ligne): https://colibri-test.herokuapp.com/api/users

URL(local): http://localhost:8080/docs/api/users

Body :{ "username": "", "password_hash": ""}

2. Authentification

For create and use the token, you must some actions:

  - Go to the authorization

  - Select the type **OAuth2.0**

  - Go to **Configure New Token -> Configuration Option** 

  - Select Grant type **Password Credentials**

  - Insert **acces token url**= https://colibri-test.herokuapp.com/token or http://localhost:8080/token ,insert **password** and **username**

  - For finish clic on **Get new access token**

  - Copy and insert the token in **access token**

3. How to test the routes

To use the differents routes, you must :

- Go to the tab **authorization** and copy your token en the **access token**

- Go to the tab **params** insert some params

- Go to the tab **body** to insert the informations in body









# Links

## fastapi +Lambda aws
- [AWS Lambda + FastAPI (Serverless Deployment): Complete CI/CD Pipeline Using GitHub Actions](https://medium.com/thelorry-product-tech-data/aws-lambda-fastapi-ci-cd-pipeline-with-github-actions-c414866b2d48#id_token=eyJhbGciOiJSUzI1NiIsImtpZCI6IjMzZmY1YWYxMmQ3NjY2YzU4Zjk5NTZlNjVlNDZjOWMwMmVmOGU3NDIiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJuYmYiOjE2NDE5OTU0MjAsImF1ZCI6IjIxNjI5NjAzNTgzNC1rMWs2cWUwNjBzMnRwMmEyamFtNGxqZGNtczAwc3R0Zy5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsInN1YiI6IjExMTE1NjMyOTgwNjk4NDk5NDczMSIsImhkIjoiZGF0YTM1NC5jbyIsImVtYWlsIjoiamV0aHJvLmRhbmhvQGRhdGEzNTQuY28iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYXpwIjoiMjE2Mjk2MDM1ODM0LWsxazZxZTA2MHMydHAyYTJqYW00bGpkY21zMDBzdHRnLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwibmFtZSI6IkpldGhybyBEYW5obyIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BQVRYQUp5Ym81SkFLTUROQ0pTSnlwNXhrT1JpaHNYLU9pdjdkX2lQOERMSj1zOTYtYyIsImdpdmVuX25hbWUiOiJKZXRocm8iLCJmYW1pbHlfbmFtZSI6IkRhbmhvIiwiaWF0IjoxNjQxOTk1NzIwLCJleHAiOjE2NDE5OTkzMjAsImp0aSI6ImZhNWQ2NTIyZTQ3YjNkYmY0ODA0YTU5OWU4YzY3ODY3Mjk0OTQzM2UifQ.IOZQaCuM-fcp62BrhcKBB71qLFj0rHRizkq-HigI80caLYM42derslpuz4mc_MXTA7h1FQvFHM11S0wjH2sPHW4SBfzeG_NAkM6jCuGmsaJ1qDHmTu6RaGPHbwXmGqVxbJ_jQVtAgb2Nt299VM30edPK0zgWofEfDMFiL4l_R7hLITXr9qCCDrsOZrlrI2ENAuiSrSPVZExifFnQHpzgwTs2Raf3YttqVVeuma9cl2HzbH4ptZcfSG1AQsYZH_nV0hHxwdzIHb1HpfLNC8VQRNZFlB0M65E5gCTE3gKMBY74yokW1UHFQITT3PAVs5pExvMtjL08vJtJb9LFAhR3WQ)

- [Simple Serverless FastAPI with AWS Lambda](https://www.deadbear.io/simple-serverless-fastapi-with-aws-lambda/)


## Amazon EKS
- [AWS EKS - Create Kubernetes cluster on Amazon EKS | the easy way](https://www.youtube.com/watch?v=p6xDCz00TxU)
- [AWS EKS | Create EKS Cluster on AWS using Console | Install Kubernetes on AWS](https://www.youtube.com/watch?v=aZd0UolVwD4)


## fastapi Auhentication
- [FastAPI Authentication Example With OAuth2, JSON Web Tokens and Tortoise ORM](https://www.youtube.com/watch?v=6hTRw_HK3Ts&t=3s)
- [FastAPI Authentication with JWT (JSON Web Tokens)](https://www.youtube.com/watch?v=0_seNFCtglk&t=2718s)