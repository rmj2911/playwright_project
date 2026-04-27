import logging  
from playwright.sync_api import expect  
from framework.config.env_selection import get_url  
from framework.fixtures.pages_fixture import pages  
  
# Get the correct URL  
url = get_url()  
logging.info(f'URL: {url}')  
  
  
def test_check_all_systems(pages):  
    logging.info("Starting test")  
  
    # Access the POM from the fixture dictionary  
    base_page = pages["base_page"]  
    system_page = pages["system_page"]  
  
    # Navigate to the URL  
    base_page.navigate(url)  
  
    logging.info("Select all checkboxes")  
    system_page.check_life_support()  
    system_page.check_navigation()  
    system_page.check_communication()  
    system_page.check_propulsion()  
  
    logging.info("Verify 'All Systems Go' is visible")  
    all_go = system_page.all_systems_go  
    expect(all_go).to_be_visible()  
  
    sys_pending = system_page.systems_pending  
    expect(sys_pending).not_to_be_visible()  
  
    logging.info("Test End")  
  
  
def test_uncheck_systems_pending(pages):  
    logging.info("Starting test")  
  
    # Access the POM from the fixture dictionary  
    base_page = pages["base_page"]  
    system_page = pages["system_page"]  
  
    # Navigate to the URL  
    base_page.navigate(url)  
  
    logging.info("Select all checkboxes")  
    system_page.check_life_support()  
    system_page.check_navigation()  
    system_page.check_communication()  
    system_page.check_propulsion()  
  
    logging.info("Deselect propulsion")  
    system_page.uncheck_propulsion()  
  
    logging.info("Verify 'Systems Pending' message")  
    sys_pending = system_page.systems_pending  
    expect(sys_pending).to_be_visible()  
  
    logging.info("Verify 'All Systems Go' message")  
    all_sys_go = system_page.all_systems_go  
    expect(all_sys_go).not_to_be_visible()  
  
    logging.info("Test End")