from fastapi import FastAPI


def configure(app: FastAPI):
    @app.get('/cars/european')
    def cars():
        return {'cars': ['lamborghini', 'ferrari', 'fusca', 'prisma']}
