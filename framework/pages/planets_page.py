# framework/pages/planets_page.py
from playwright.sync_api import Page

class PlanetsPage:
    def __init__(self, page: Page):
        self.page = page
        self.planet_input = page.locator("[id='planet-input']")
        self.planet_submit = page.locator("[id='planet-submit']")
        self.planet_popup = page.locator("[id='planet-popup']")

    def fill_planet_name(self, name):
        self.planet_input.fill(name)

    def submit_planet(self):
        self.planet_submit.click()

    def get_popup_text(self):
        return self.planet_popup.inner_text()