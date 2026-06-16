from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.schemas.twin_schema import BasicInfoRequest, BasicInfoResponse
from app.services.twin_service import create_twin

router = APIRouter(
    prefix="/api/twin",
    tags=["Twin"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post(
    "/basic-info",
    response_model=BasicInfoResponse
)
def save_basic_info(
    twin_data: BasicInfoRequest,
    db: Session = Depends(get_db)
):
    return create_twin(db, twin_data)
