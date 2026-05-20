from fastapi import APIRouter
from fastapi import UploadFile, File
from fastapi.responses import FileResponse

from app.services.cleaner import clean_dataset
from app.utils.file_handler import save_file

router = APIRouter()

@router.post("/clean")

async def clean_api(
    file: UploadFile = File(...)
):

    input_path = save_file(file)

    output_path = clean_dataset(
        input_path
    )

    return FileResponse(
        output_path,
        media_type="text/csv",
        filename="cleaned_data.csv"
    )