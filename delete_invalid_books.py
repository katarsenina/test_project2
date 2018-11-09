import requests
import unittest

class TestDeleteBooks(unittest.TestCase):
    '''Delete invalid books test'''

    def setUp(self):
        self.base_url = "http://pulse-rest-testing.herokuapp.com/"
        self.book_url = self.base_url + "books/"
        self.book_data = {"title": "LAMA", "author": "Alex Bilouss"}

    def test_delete_invalid_books(self):
        for i in range (1986, 2028):
            resp_del = requests.delete(self.book_url + str(i))

    def tearDown(self):
        for i in range(1986, 2028):
            resp = requests.get(self.book_url + str(i))
            self.assertEqual(resp.status_code, 404)

if __name__ == "__main__":

    unittest.main(verbosity=2)
