import main
from fastapi.testclient import TestClient
from faker import Faker

client = TestClient(main.app)
fake = Faker()
## test main
def test_main_resource():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to API COLIBRI"}


## test create user
def test_create_user():
    headers = {"Content-type": "application/json"}
    user = dict()
    user["username"] = fake.user_name()
    print(" ########################")
    print(fake.user_name())
    user["password_hash"] = "aziz"
    response = client.post("/api/users", json=user, headers=headers)
    assert response.status_code == 200


# ## test create user
# def test_create_exist_user():
#     headers = {'Content-type': 'application/json'}
#     user=dict()
#     user['username']="aziz"
#     user['password_hash']="aziz"
#     response = client.post("/api/users",json=user,headers=headers)
#     assert response.status_code == 401
#     assert response.json()=={"detail":"user already exist"}

## test authentification
def test_authentification():
    response = client.post("/token", data={"username": "aziz", "password": "aziz"})
    assert response.status_code == 200


## test unauthenfication
def test_unauthentifaction():
    response = client.post("/token", data={"username": "azizou", "password": "aziz"})
    assert response.status_code == 401


## test upload taxpayer
def test_upload_taxpayer_info():
    response = client.post(
        "/api/upload_taxpayer_info/?id=azi&type=photo_id",
        files={"file": ("file.jpg", open("az.jpg", "rb"), "image/jpg")},
        headers={
            "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjNzNlkzbzdRUk93UmtiMXplM2l6IiwidXNlcm5hbWUiOiJheml6IiwicGFzc3dvcmRfaGFzaCI6IiQyYiQxMiRsVGI2S3RGZk9MQlJPTlZCb2tRYlNlemdXUGZ4WUxnTkFLc3BRSnlPb2cwNXRwYUtZdlFyZSJ9.mFNVcLMeFhuleJI3g4CwVuxpqrhqYEOW44TlEM2NkjY"
        },
    )
    assert response.status_code == 200


## test download activity
def test_upload_activity_info():
    response = client.post(
        "/api/upload_activity_info/?id=az&type=photo_activity",
        files={"file": ("file.jpg", open("az.jpg", "rb"), "image/jpg")},
        headers={
            "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjNzNlkzbzdRUk93UmtiMXplM2l6IiwidXNlcm5hbWUiOiJheml6IiwicGFzc3dvcmRfaGFzaCI6IiQyYiQxMiRsVGI2S3RGZk9MQlJPTlZCb2tRYlNlemdXUGZ4WUxnTkFLc3BRSnlPb2cwNXRwYUtZdlFyZSJ9.mFNVcLMeFhuleJI3g4CwVuxpqrhqYEOW44TlEM2NkjY"
        },
    )
    assert response.status_code == 200


## test download activity
def test_download_activity_info():
    response = client.get(
        "/api/download_activity_info/?id=az&type=photo_activity",
        headers={
            "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjNzNlkzbzdRUk93UmtiMXplM2l6IiwidXNlcm5hbWUiOiJheml6IiwicGFzc3dvcmRfaGFzaCI6IiQyYiQxMiRsVGI2S3RGZk9MQlJPTlZCb2tRYlNlemdXUGZ4WUxnTkFLc3BRSnlPb2cwNXRwYUtZdlFyZSJ9.mFNVcLMeFhuleJI3g4CwVuxpqrhqYEOW44TlEM2NkjY"
        },
    )
    assert response.status_code == 200


## test download taxpayer
def test_download_taxpayer_info():
    response = client.get(
        "/api/download_taxpayer_info/?id=az&type=photo_id",
        headers={
            "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjNzNlkzbzdRUk93UmtiMXplM2l6IiwidXNlcm5hbWUiOiJheml6IiwicGFzc3dvcmRfaGFzaCI6IiQyYiQxMiRsVGI2S3RGZk9MQlJPTlZCb2tRYlNlemdXUGZ4WUxnTkFLc3BRSnlPb2cwNXRwYUtZdlFyZSJ9.mFNVcLMeFhuleJI3g4CwVuxpqrhqYEOW44TlEM2NkjY"
        },
    )
    assert response.status_code == 200
