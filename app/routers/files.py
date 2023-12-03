from datetime import datetime
import secrets
from fastapi import APIRouter, Depends, File, UploadFile
from bson.objectid import ObjectId
from app.serializers.userSerializers import userResponseEntity

from app.database import File as FileDB
from .. import oauth2, schemas
from ..config import settings

router = APIRouter()

@router.post("/upload", response_model=schemas.FileResponseSchema)
async def upload_file(file: UploadFile = File(...), user_role: str = Depends(oauth2.require_role)):
    valid_extensions = ["docx", "pptx", "xlsx"]

    if user_role != "admin":
        return {"message": "You are not authorized to upload files"}
    
    FILEPATH = "./static/"
    filename = file.filename
    extension = filename.split(".")[-1]

    if extension not in valid_extensions:
        return {"message": "Invalid file type"}
    
    token_name = secrets.token_hex(16) + "." + extension
    generated_name = FILEPATH + "/" + token_name
    file_content = await file.read()

    result = FileDB.insert_one({"name": file.filename, "url_token": token_name, "created_at": datetime.utcnow(), "updated_at": datetime.utcnow()})

    with open(generated_name, "wb") as file:
        file.write(file_content)
        file.close()
    
    file_url = settings.API_URL + "/static/" + token_name
    return {"message": "File uploaded successfully", "file_name": file_url, "file_id": str(result.inserted_id), "created_at": datetime.utcnow(), "updated_at": datetime.utcnow()}

@router.get("/list", response_model=schemas.FileListResponse)
async def list_files(user_role: str = Depends(oauth2.require_role)):
    files = FileDB.find()
    files_list = []

    for file in files:
        files_list.append({"file_name": file["name"], "file_id": str(file["_id"]), "created_at": file["created_at"], "updated_at": file["updated_at"]})

    return {"message": "Files retrieved successfully", "files": files_list}
    
@router.get("/view/{file_id}", response_model=schemas.FileResponse)
async def view_file(file_id: str, user_role: str = Depends(oauth2.require_role)):
    file = FileDB.find_one({"_id": ObjectId(file_id)})
    if not file:
        return {"message": "File not found"}
    file_url = settings.API_URL + "/static/" + file["url_token"]
    return {"message": "File retrieved successfully", "download_link": file_url}