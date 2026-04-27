# framework/fixtures/pages_fixture.py
import pytest  
from playwright.sync_api import Page  
from framework.pages.base_page import BasePage  
from framework.pages.planets_page import PlanetsPage  
from framework.pages.system_checks_page import SystemChecksPage  
  
  
@pytest.fixture(scope="function")  
def pages(page: Page):  
    web_page = {  
        "base_page": BasePage(page),  
        "planets_page": PlanetsPage(page),  
        "system_page": SystemChecksPage(page),  
    }  
  
    return web_page