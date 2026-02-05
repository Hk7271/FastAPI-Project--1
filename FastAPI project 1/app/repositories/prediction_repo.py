from sqlalchemy.orm import Session

from app.models.prediction import IrisPrediction

def create_prediction(db: Session, data, prediction: str):
    record = IrisPrediction(
        sepal_length=data.sepal_length,
        sepal_width=data.sepal_width,
        petal_length=data.petal_length,
        petal_width=data.petal_width,
        prediction=prediction,
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return record
def get_all_predictions(db: Session):
    return db.query(IrisPrediction).all()

def get_prediction_by_id(db: Session, record_id: int):
    return(
        db.query(IrisPrediction)
        .filter(IrisPrediction.id == record_id)
        .first()

    )

def update_prediction(db: Session, record, data, prediction: str):
    record.sepal_length = data.sepal_length
    record.sepal_width = data.sepal_width
    record.petal_length = data.petal_length
    record.petal_width = data.petal_width
    record.prediction = prediction

    db.commit()
    db.refresh(record)
    return record

def delete_prediction(db: Session,record):
    db.delete(record)
    db.commit()    
