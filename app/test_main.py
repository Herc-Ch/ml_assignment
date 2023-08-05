import pytest
from starlette.testclient import TestClient

from app.main import app




@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client

def test_health(test_app):
    response = test_app.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "UP"}

def test_features(test_app):
    test_feature_dummy_data = {"data":[{"customer_ID":"1090","loans":[{"customer_ID":"1090","loan_date":"15/11/2021","amount":"2426","fee":"199","loan_status":"0","term":"long","annual_income":"41333"}]}]}
    test_feature_result_data = [{"customer_ID":"1090","loan_date":"2021-11-15T00:00:00","amount":2426,"fee":199,"loan_status":"0","term":"long","annual_income":"41333","year":2021}]
    response = test_app.post("/feature_engineering", json=test_feature_dummy_data)
    assert response.status_code == 200
    assert response.json() == test_feature_result_data

