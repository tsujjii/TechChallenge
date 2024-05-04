from fastapi import FastAPI
from .router import processing_router, production_router, commercialization_router, import_router, export_router

app = FastAPI()

app.include_router(production_router, tags=["v1"])
app.include_router(processing_router, tags=["v1"])
app.include_router(commercialization_router, tags=["v1"])
app.include_router(import_router, tags=["v1"])
app.include_router(export_router, tags=["v1"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)