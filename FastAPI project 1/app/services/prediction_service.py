import joblib
from pathlib import Path
from sqlalchemy.orm import Session

from app.repositories import prediction_repo
from app.schemas.prediction import IrisCreate, IrisUpdate

Model_Path = Path(__file__).resolve().parents[1] / "model.pkl"

model = joblib.load(Model_Path)

flower_map = {
    0: "Setosa",
    1: "Versicolor",
    2: "Virginica",
}

def _predict_label(data):
    features = [[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width,
    ]]

    prediction = model.predict(features)[0]
    return flower_map [int(prediction)]

def create_prediction_service (db: Session, data: IrisCreate):
    label = _predict_label(data)
    return prediction_repo.create_prediction(db, data, label)

def update_prediction_service (db:Session, record, data: IrisUpdate):
    label = _predict_label(data)
    return prediction_repo.update_prediction(db, record, data, label)
