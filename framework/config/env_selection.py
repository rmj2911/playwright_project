# framework/config/env_selection.py  
from dotenv import load_dotenv, find_dotenv  
import os  
  
# Automatically finds and loads the .env file
env_file = find_dotenv()
load_dotenv(env_file)  
  
# URLs for different environments  
url_qa = "https://ch-matviy.github.io/space-test-automation-practice-page-qa/"  
url_dev = "https://ch-matviy.github.io/space-test-automation-practice-page-dev/"  
  
  
def get_url():  
    # Get the environment variable from .env  
    env = os.getenv('TEST_ENV')  
  
    # Return the corresponding URL  
    if env == "qa":  
        return url_qa  
    else:  
        return url_dev