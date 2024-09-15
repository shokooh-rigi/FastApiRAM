from fastapi.testclient import TestClient
from application.tests.factories import RAMInfoFactory
from main import app

client = TestClient(app)


def test_save_ram_info_endpoint():
    """
    Test the /save-ram-info endpoint for saving RAM info.
    """
    # Given
    ram_info_data = {
        "total": 16384.0,
        "free": 8192.0,
        "used": 8192.0,
        "timestamp": "2024-09-10T10:00:00"
    }
    # When
    response = client.get("/ram/save-ram-info")
    # Then
    assert response.status_code == 200


def test_get_last_n_records_endpoint():
    """
    Test the /ram-info/{n} endpoint for retrieving the last n RAM records.
    """
    # Given
    for _ in range(5):
        RAMInfoFactory.create()
    # When
    response = client.get("/ram/ram-info/3")  # Ensure this matches your handler
    # Then
    assert response.status_code == 200
    # assert len(response.json()) == 3
