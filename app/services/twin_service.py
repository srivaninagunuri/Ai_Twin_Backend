from sqlalchemy.orm import Session
from app.models.twin_model import Twin
from app.schemas.twin_schema import BasicInfoRequest


def create_twin(db: Session, twin_data: BasicInfoRequest):
    new_twin = Twin(
        twin_name=twin_data.twin_name,
        brand_description=twin_data.brand_description
    )

    db.add(new_twin)
    db.commit()
    db.refresh(new_twin)

    return new_twin