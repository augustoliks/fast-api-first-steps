def create_app():
    from fastapi import FastAPI
    from routes import register_routes

    app = FastAPI()

    register_routes(app)

    return app


app = create_app()
