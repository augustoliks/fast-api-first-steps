from fastapi import FastAPI


def configure(app: FastAPI):
    @app.get('/cities/brazil')
    def cities():
        return {'city': ['jacarei', 'sao jose dos campos', 'pindamonhangaba', 'campinas']}
