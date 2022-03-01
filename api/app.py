from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from typing import Optional
from datetime import datetime
from database.db import *

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
