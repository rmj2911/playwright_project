import logging

from playwright.sync_api import Playwright

from framework.config.env_selection import get_url


def test_space_page_api_smoke(playwright: Playwright):
    """GET the configured Space practice page URL and assert basics on the response."""
    url = get_url()
    logging.info("Starting API smoke test")
    logging.info(f"URL: {url}")

    request_context = playwright.request.new_context()
    try:
        response = request_context.get(url)
        logging.info(f"Response status: {response.status}")
        assert response.ok, f"Expected 2xx, got {response.status}"

        content_type = response.headers.get("content-type", "")
        logging.info(f"Content-Type: {content_type}")
        assert "text/html" in content_type.lower()

        body = response.text()
        assert "Space Test Automation Practice" in body
        logging.info("Verified page marker in response body")
    finally:
        request_context.dispose()

    logging.info("API smoke test end")
