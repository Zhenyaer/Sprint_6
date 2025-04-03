import pytest
from selenium import webdriver
from src.config import URL


@pytest.fixture
def driver():
    firefox = webdriver.Firefox()
    firefox.maximize_window()
    firefox.get(URL.url_main_page)
    yield firefox
    firefox.quit()
