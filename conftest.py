import pytest
import requests


@pytest.fixture(scope="session")
def base_url():
    return "http://pulse-rest-testing.herokuapp.com/"


@pytest.fixture()
def book_data(base_url):
    book = {"title": "Anna Karenina", "author": "Lev Tolstoy"}
    return book
    # requests.delete(base_url + "books/" + str(b["id"]))


@pytest.fixture(scope="session", autouse=True)
def clean_book_id(base_url):
    clean_book_id = []
    yield clean_book_id
    print(clean_book_id)
    # TODO: clean all using these ids


@pytest.fixture()
def book(base_url):
    """ Fixture of already created book for roles testing """
    r = requests.post(base_url + "books/", data={"title": "A", "author": "B"})
    return r.json()
