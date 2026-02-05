from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.schemas.prediction import IrisCreate, IrisUpdate, IrisResponse
from app.repositories import prediction_repo
from app.services.prediction_service import(
    create_prediction_service,
    update_prediction_service,
)

router = APIRouter(prefix="/predictions",tags=["Predictions"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/",response_model=IrisResponse)
def create_prediction(data: IrisCreate, db: Session = Depends(get_db)):
    return create_prediction_service(db, data)

@router.get("/", response_model=list[IrisResponse])
def list_predictions(db: Session = Depends(get_db)):
    return prediction_repo.get_all_predictions(db)

@router.put("/{record_id}", response_model=IrisResponse)
def update_prediction(
    record_id: int, data: IrisUpdate, db: Session = Depends(get_db)
):
    record = prediction_repo.get_prediction_by_id(db, record_id)
    if not record:
        raise HTTPException(status_code=404, detail="Prediction not found")
    return update_prediction_service(db, record, data)

@router.delete("/{record_id}")
def delete_prediction(record_id: int, db: Session = Depends(get_db)):
    record = prediction_repo.get_prediction_by_id(db, record_id)
    if not record:
        raise HTTPException(status_code=404, detail="Prediction not found")
    prediction_repo.delete_prediction(db, record)
    return {"message": "Record deleted successfully"}