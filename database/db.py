from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from .models import Base, Field, FieldData

engine = create_engine("postgresql+psycopg2://kmg:qwerty123@127.0.0.1:10001/kmg")
Session = sessionmaker(bind=engine)
session = Session()


class BadRequest(Exception):
    pass


def initialize_database():
    Base.metadata.create_all(engine)


def drop_database():
    Base.metadata.drop_all(engine)


def add_field(name: str) -> int:
    field = session.query(Field).filter(Field.name == name).first()
    if not field:
        field = Field(name=name)
        session.add(field)
        session.commit()
    return field.id


def save_field_data(instances: list):
    session.add_all(instances)
    try:
        session.commit()
    except IntegrityError:
        session.rollback()
        print("Data already exist in db.")
    return {"status": "Success", "message": "Success"}


def get_positive_field_data(field_id: int, start, finish) -> list:
    query = session.query(FieldData).filter(FieldData.field_id == field_id)\
        .filter(FieldData.start_datetime >= start)\
        .filter(FieldData.start_datetime <= finish)\
        .filter(FieldData.value != 0)
    return query.all()


def get_negative_field_data(field_id: int, start, finish) -> list:
    query = session.query(FieldData).filter(FieldData.field_id == field_id) \
        .filter(FieldData.start_datetime >= start) \
        .filter(FieldData.start_datetime <= finish) \
        .filter(FieldData.value == 0)
    return query.all()
