
import unittest


from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()


    def test_ping(self):
        response = self.client.get('/ping')
        self.assertEqual(response.status_code, 200)


    def test_system(self):
        response = self.client.get('/system')
        self.assertEqual(response.status_code, 200)

    def test_media_info_pass(self):
        response = self.client.get('/mediainfo/11497188')
        self.assertEqual(response.status_code, 200)

    def test_media_info_fail(self):
        response = self.client.get('/mediainfo/')
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
