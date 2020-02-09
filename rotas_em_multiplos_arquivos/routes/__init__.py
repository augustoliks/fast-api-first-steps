from fastapi import FastAPI


def register_routes(app: FastAPI):
    from . import peoples, cities, cars

    cars.configure(app)
    peoples.configure(app)
    cars.configure(app)
