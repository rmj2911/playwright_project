# framework/pages/system_checks_page.py
from playwright.sync_api import Page

class SystemChecksPage:
    def __init__(self, page: Page):
        self.page = page
        self.life_support_checkbox = page.locator("#life-support-check")
        self.navigation_checkbox = page.locator("#navigation-check")
        self.communication_checkbox = page.locator("#communication-check")
        self.propulsion_checkbox = page.locator("#propulsion-check")
        self.all_systems_go = page.locator("#all-systems-go")
        self.systems_pending = page.locator("#systems-pending")

    def is_life_support_checked(self):
        return self.life_support_checkbox.is_checked()

    def is_navigation_checked(self):
        return self.navigation_checkbox.is_checked()

    def is_communication_checked(self):
        return self.communication_checkbox.is_checked()

    def is_propulsion_checked(self):
        return self.propulsion_checkbox.is_checked()

    def is_all_systems_go_visible(self):
        return self.all_systems_go.is_visible()

    def is_systems_pending_visible(self):
        return self.systems_pending.is_visible()

    def check_life_support(self):
        self.life_support_checkbox.check()

    def check_navigation(self):
        self.navigation_checkbox.check()

    def check_communication(self):
        self.communication_checkbox.check()

    def check_propulsion(self):
        self.propulsion_checkbox.check()

    def uncheck_propulsion(self):
        self.propulsion_checkbox.uncheck()