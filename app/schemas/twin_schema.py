from pydantic import BaseModel


class BasicInfoRequest(BaseModel):
    twin_name: str
    brand_description: str


class BasicInfoResponse(BaseModel):
    id: int
    twin_name: str
    brand_description: str

    class Config:
        from_attributes = True