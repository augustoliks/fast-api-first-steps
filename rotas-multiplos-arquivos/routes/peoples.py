from fastapi import FastAPI


def configure(app: FastAPI):
    @app.get('/peoples/females')
    def peoples():
        return {'peoples': ['ana', 'mariana', 'julieta', 'marieta']}
