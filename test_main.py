import unittest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestMain(unittest.TestCase):
    
    def test_temperature_endpoint(self):
        response = client.get("/temperature")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("temperature" in response.json())
    
    def test_rain_endpoint(self):
        response = client.get("/rain")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("rain" in response.json())

if __name__ == "__main__":
    unittest.main()