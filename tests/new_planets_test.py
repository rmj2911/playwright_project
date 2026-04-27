import logging  
from playwright.sync_api import expect  
from framework.utils.helpers import load_planet_name  
from framework.fixtures.pages_fixture import pages  
from framework.config.env_selection import get_url  
  
# Get the correct URL  
url = get_url()  
  
  
def test_add_a_planet(pages):  
    logging.info("Starting test")  
    logging.info(f'URL: {url}')  
  
    # Access the POM
    base_page = pages["base_page"]  
    planets_page = pages["planets_page"]  
  
    # Get data from a JSON  
    new_planet = load_planet_name("planetName")  
  
    # Navigate to the URL  
    base_page.navigate(url)  
  
    logging.info(f'Input Planet: {new_planet}')  
    planet_input = planets_page.planet_input  
    expect(planet_input).to_be_visible()  
    planets_page.fill_planet_name(new_planet)  
  
    logging.info("Click Submit")  
    planet_submit = planets_page.planet_submit  
    expect(planet_submit).to_be_enabled()  
    planets_page.submit_planet()  
  
    logging.info("Verify Confirmation text")  
    expect(planets_page.planet_popup).to_be_visible()  
  
    expected_text = f"New planet added: {new_planet}"  
    current_text = planets_page.planet_popup  
    expect(current_text).to_have_text(expected_text)  
  
    logging.info("Test End")