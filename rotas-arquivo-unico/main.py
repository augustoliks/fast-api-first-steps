from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app = FastAPI()


class City(BaseModel):
    street: str = 'Rua Ramalhete'


class People(BaseModel):
    name: str
    price: float
    is_offer: bool = None
    address: List[City]


@app.get('/')
def root():
    return {'message': 'hello world'}


@app.put('/')
def insert_people(name: str, age: int):
    return {'message': 'hello world'}


@app.post('/')
def post_people(people: People):
    return {'message': 'hello world'}
