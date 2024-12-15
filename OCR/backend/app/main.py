from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import shutil
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="OCR Forms API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

STORAGE_PATH = Path("storage")
UPLOAD_PATH = STORAGE_PATH / "uploads"
PROCESSED_PATH = STORAGE_PATH / "processed"

for path in [UPLOAD_PATH, PROCESSED_PATH]:
    path.mkdir(parents=True, exist_ok=True)

@app.post("/api/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        file_path = UPLOAD_PATH / file.filename
        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return {"filename": file.filename, "status": "success"}
    except Exception as e:
        logger.error(f"Upload error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
