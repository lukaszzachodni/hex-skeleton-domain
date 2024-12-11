import unittest


from src.main import app  # Importujemy app po dodaniu ścieżki


class TestMain(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_helloworld(self):
        response = self.app.get("/helloworld")
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json)
        self.assertIn("datetime", response.json)
        self.assertEqual(response.json["message"], "hello world")


if __name__ == "__main__":
    unittest.main()
