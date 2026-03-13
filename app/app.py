from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
import traceback
import os
from dotenv import load_dotenv

from app.prediction_api import router

# Load environment variables
load_dotenv()

HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 8000))
LOG_LEVEL = os.getenv("LOG_LEVEL", "info")
PYTHON_ENV = os.getenv("PYTHON_ENV", "development")


app = FastAPI(
    title="Customer Churn Prediction API",
    version="1.0"
)

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(router)


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    """Catch all unhandled exceptions and return JSON"""
    error_msg = str(exc)
    print(f"Unhandled error: {error_msg}")
    print(traceback.format_exc())
    
    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        return JSONResponse(
            {"error": error_msg, "detail": traceback.format_exc()},
            status_code=500
        )
    
    return JSONResponse(
        {"error": error_msg},
        status_code=500
    )


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
