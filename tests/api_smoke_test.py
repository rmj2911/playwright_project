import logging
from urllib.parse import urljoin

from playwright.sync_api import Playwright

from framework.config.env_selection import get_url


def test_space_page_api_smoke_returns_expected_html(playwright: Playwright):
    """GET the configured Space practice page URL and assert basics on the response."""
    url = get_url()
    logging.info("Starting API smoke test")
    logging.info(f"URL: {url}")

    request_context = playwright.request.new_context()
    try:
        response = request_context.get(url)
        logging.info(f"Response status: {response.status}")
        assert response.ok, f"Expected 2xx, got {response.status}"
        assert response.status == 200

        content_type = response.headers.get("content-type", "")
        logging.info(f"Content-Type: {content_type}")
        assert "text/html" in content_type.lower()

        body = response.text()
        assert "Space Test Automation Practice" in body
        logging.info("Verified page marker in response body")
    finally:
        request_context.dispose()

    logging.info("API smoke test end")


def test_space_page_missing_path_returns_not_ok(playwright: Playwright):
    """GET a known-missing path under the configured URL and assert it is not served as OK."""
    missing_url = urljoin(get_url(), "__missing_api_smoke_probe__")
    logging.info("Starting missing-path smoke test")
    logging.info(f"URL: {missing_url}")

    request_context = playwright.request.new_context()
    try:
        response = request_context.get(missing_url)
        logging.info(f"Response status: {response.status}")
        assert not response.ok, f"Expected missing path to be non-OK, got {response.status}"
        assert response.status == 404
    finally:
        request_context.dispose()

    logging.info("Missing-path smoke test end")
