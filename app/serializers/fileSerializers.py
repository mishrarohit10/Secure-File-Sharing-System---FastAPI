def fileEntity(file) -> dict:
    return {
        "id": str(file["_id"]),
        "name": file["name"],
        "url_token": file["url_token"],
        "created_at": file["created_at"],
        "updated_at": file["updated_at"]
    }


def fileResponseEntity(file) -> dict:
    return {
        "id": str(file["_id"]),
        "name": file["name"],
        "url_token": file["url_token"],
        "created_at": file["created_at"],
        "updated_at": file["updated_at"]
    }


def fileListEntity(files) -> list:
    return [fileEntity(file) for file in files]
