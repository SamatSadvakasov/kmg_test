from fastapi import FastAPI, UploadFile, File
from fastapi.responses import RedirectResponse
from typing import Optional
from datetime import datetime
from database.db import *
from parsing.parse import parsing_uploaded_file

app = FastAPI()


@app.get("/")
def read_root():
    """SWAGGER"""
    return RedirectResponse(url='/docs')


@app.get("/fields/{field_id}/data")
def get_field_data_handle(field_id: Optional[int] = 1,
                          negative: Optional[bool] = False,
                          start_time: Optional[str] = datetime(2020, 6, 3, 17, 58, 16).strftime("%Y-%m-%d %H:%M:%S"),
                          finish_time: Optional[str] = datetime(2020, 6, 3, 17, 58, 36).strftime("%Y-%m-%d %H:%M:%S")):
    """Получить данные месторождения по идентификатору"""
    start = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    finish = datetime.strptime(finish_time, "%Y-%m-%d %H:%M:%S")
    if negative:
        return get_negative_field_data(field_id, start, finish)
    return get_positive_field_data(field_id, start, finish)


@app.post("/upload-file/")
async def create_upload_file(uploaded_file: UploadFile = File(...)):
    file_location = 'parsing/uploaded_files/' + uploaded_file.filename
    with open(file_location, "wb+") as file_object:
        file_object.write(uploaded_file.file.read())
    parsing_uploaded_file(file_location, uploaded_file.filename)
    return {"info": f"file '{uploaded_file.filename}' saved at '{file_location}'"}

