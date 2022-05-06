from anyio import Path
from fastapi import APIRouter, File, Depends, UploadFile
import datetime
from ..model.user import User
from ..service.auth import get_current_user
from ..service.file_service import (
    save_file_to_storage,
    download_file_to_storage,
    verify_file_existance,
    generate_qrcode,
)

router = APIRouter()
DT_FMT_FN = "%Y%m%d%H%M%S"


# save qrcode
def save_qrcode(id: str):
    """this function saves the qrcode of the activity to cloud storage
    Args:
        id (str): Id of the activity
    """
    output_folder = "ACTIVITY/Activity-" + id + "/qrcode/"
    output_fn = datetime.datetime.utcnow().strftime(DT_FMT_FN)
    image_url = output_folder + output_fn
    number = int(id)
    public_key = number + 3000000 + (number * 2)
    # qrcode url
    url = "https://crystal-service-siews7qsrq-ue.a.run.app/login?pid=" + str(public_key)
    image = generate_qrcode(url)
    ##Save qrcode to s3
    save_file_to_storage(image_url, image)


# Endpoint to store image taxpayer on Cloud Storage
@router.post("/upload_taxpayer_info/", tags=["Upload taxpayer file to CLoud Storage"])
async def create_taxpayer_file(
    id: str,
    type: str,
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
):
    """This route upload the file of the taxpayer to cloud storage
    Args:
        id (str): Id of the taxpayer
        type (str): type of the file
        file (UploadFile, optional): content the file. Defaults to File(...).
        current_user (User, optional): content the user information. Defaults to Depends(get_current_user).
    """
    if type not in ["photo_id", "face_id", "certificate"]:
        return {"message": "Type not exist", "code": "0"}
    output_folder = "TAXPAYER/Taxpayer-" + id + "/" + type + "/"
    output_fn = datetime.datetime.utcnow().strftime(DT_FMT_FN)
    image_url = output_folder + output_fn
    # save the file
    save_file_to_storage(image_url, file)
    return {"message": "File upload to Cloud Storage ", "code": "1"}


# Endpoint to download taxpayer image from Cloud Storage
@router.get("/download_taxpayer_info/", tags=["Upload taxpayer file to CLoud Storage"])
async def get_taxpayer_file(
    id: str, type: str, current_user: User = Depends(get_current_user)
):
    """This function downloads the file of the taxpayer to cloud storage
    Args:
        id (str): Id of taxpayer
        type (str): type of file
        current_user (User, optional): user informations. Defaults to Depends(get_current_user).
    Returns:
        url: image url for the file download
    """
    if type not in ["photo_id", "face_id", "certificate"]:
        return {"message": "Type not exist", "code": "0"}
    output_folder = "TAXPAYER/Taxpayer-" + id + "/" + type + "/"
    if not verify_file_existance(output_folder):
        return {"message": "File not exist", "code": "-1"}
    url = download_file_to_storage(output_folder)
    download_file_to_storage(output_folder)
    return {"message": "success", "code": "1", "image_url": url}


# Endpoint to store image activity on Cloud Storage
@router.post("/upload_activity_info/", tags=["Upload activity file to CLoud Storage"])
async def create_activity_file(
    id: str,
    type: str,
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
):

    """This route upload the file of the activity to cloud storage
    Args:
        id (str): Id of the activity
        type (str): type of the file
        file (UploadFile, optional): content the file. Defaults to File(...).
        current_user (User, optional): content the user information. Defaults to Depends(get_current_user).
    """
    if type not in ["photo_activity", "cadaster", "certificate"]:
        return {"message": "Type not exist", "code": "0"}
    output_folder = "ACTIVITY/Activity-" + id + "/" + type + "/"
    output_fn = datetime.datetime.utcnow().strftime(DT_FMT_FN)
    image_url = output_folder + output_fn
    # Save to s3
    save_file_to_storage(image_url, file)
    return {"message": "File upload to cloud storage", "code": "1"}


# Endpoint to download taxpayer image from Cloud Storage
@router.get("/download_activity_info/", tags=["Upload activity file to CLoud Storage"])
async def get_activity_image(
    id: str, type: str, current_user: User = Depends(get_current_user)
):
    """This function downloads the file of the activity to cloud storage
    Args:
        id (str): Id of activity
        type (str): type of file
        current_user (User, optional): user informations. Defaults to Depends(get_current_user).
    Returns:
        url: image url for the file download
    """
    if type not in ["photo_activity", "cadaster", "certificate"]:
        return {"message": "Type not exist", "code": "0"}
    output_folder = "ACTIVITY/Activity-" + id + "/" + type + "/"
    if not verify_file_existance(output_folder):
        return {"message": "File not exist", "code": "-1"}
    url = download_file_to_storage(output_folder)
    return {"message": "success", "code": "1", "image_url": url}
