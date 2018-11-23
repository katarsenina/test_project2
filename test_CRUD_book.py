import requests
import unittest


class TestBooks(unittest.TestCase):
    '''Create, edit and delete tests for book'''

    @classmethod
    def setUpClass(cls):
        cls.base_url = "http://pulse-rest-testing.herokuapp.com/"
        cls.book_url = cls.base_url + "books/"

    def setUp(self):
        self.book_data = {"title": "LAMA", "author": "Alex Bilouss"}

    def test_create_book(self):
        resp = requests.post(self.book_url, data=self.book_data)
        self.assertEqual(resp.status_code, 201)         # проверяем, что книга создана
        resp_data = resp.json()                         # проверяем, что id находится в
        self.assertIn("id", resp_data)                  # словаре данных созданной книги
        self.book_data["id"] = resp_data["id"]          # присваиваем айдишку нашим данным
        # print(self.book_data["id"])

        for key in resp_data:                           # проверяем, что значения ключей совпадают
            self.assertEqual(self.book_data[key], resp_data[key])


        resp_e = requests.put(self.book_url + str(self.book_data["id"]),
                              data={"author": "Benedict"})
        self.assertEqual(resp_e.status_code, 200)
        # print(resp_e.text)

    def tearDown(self):
        resp_del = requests.delete(self.book_url + str(self.book_data["id"]))
        self.assertEqual(resp_del.status_code, 204)
        resp = requests.get(self.book_url + str(self.book_data["id"]))
        self.assertEqual(resp.status_code, 404)


if __name__ == "__main__":
    unittest.main(verbosity=2)
