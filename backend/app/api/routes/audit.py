from fastapi import APIRouter, UploadFile, File, HTTPException
from uuid import uuid4

router = APIRouter(prefix="/api/v1", tags=["Audit"])

@router.post("/audit")
async def create_audit(image: UploadFile = File(...)):
    
    # Validate the uploaded file
    if not image.content_type or not image.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Please upload a valid image.")

    # Read the image
    image_bytes = await image.read()

    if not image_bytes:
        raise HTTPException(status_code=400, detail="The uploaded image is empty.")

    # Temporary mock result
    return {
        "audit_id": str(uuid4()),
        "status": "completed",
        "product": {
            "name": "Sample Food Product",
            "ingredients": [
                "Sugar",
                "Wheat flour",
                "Vegetable oil"
            ]
        },
        "nutrition": {
            "calories": 250,
            "sugar_g": 18
        },
        "warnings": [
            {
                "type": "nutrition",
                "message": "Sample high-sugar warning"
            }
        ],
        "summary": "This is a mock audit. OCR and RAG are not connected yet."
    }
    
    # This is a temporary implementation. It checks that an image was uploaded and returns sample data. It doesn't yet analyze the image.