import unittest
from fastapi.testclient import TestClient
import app  # Assuming your main file is app.py


class TestAPI(unittest.TestCase):
    def test_books_endpoint(self):
        tester = TestClient(app.app)
        response = tester.get("/books")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Rich Dad Poor Dad", response.json())

    def test_health_endpoint(self):
        tester = TestClient(app.app)
        response = tester.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})


if __name__ == "__main__":
    unittest.main()
