from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

import pandas as pd
import shutil
import os

from app.services.cleaner import clean_dataset
from app.services.analyzer import analyze_dataset
from app.services.ollama_service import predict_algorithm

router = APIRouter()

@router.post("/predict")

async def predict_model(

    file: UploadFile = File(...)
):

    upload_path = os.path.join(
        "app",
        "uploads",
        file.filename
    )

    with open(upload_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    # Clean dataset
    cleaned_path = clean_dataset(
        upload_path
    )

    # Read cleaned CSV
    df = pd.read_csv(
        cleaned_path
    )

    # Analyze dataset
    analysis = analyze_dataset(df)

    # Predict algorithm
    result = predict_algorithm(
        analysis
    )

    return {

        "analysis": analysis,
        "prediction": result
    }