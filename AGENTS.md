# Purpose

This repository is a Python UI test automation framework for the Space Test Automation Practice pages. The existing tests validate adding a new planet and spacecraft system-check behavior against DEV or QA URLs.

# Repository structure

- `tests/`: pytest test files for UI flows.
- `tests/new_planets_test.py`: validates adding a planet and confirming the success popup text.
- `tests/spacecraft_test.py`: validates spacecraft checkbox states and the "All Systems Go" / "Systems Pending" messages.
- `framework/pages/`: Page Object Model classes that hold Playwright locators and page actions.
- `framework/pages/base_page.py`: shared navigation and title helpers.
- `framework/pages/planets_page.py`: page object for the planet input, submit button, and popup.
- `framework/pages/system_checks_page.py`: page object for spacecraft system checkboxes and status messages.
- `framework/fixtures/pages_fixture.py`: function-scoped pytest fixture that returns a dictionary of page object instances keyed by `"base_page"`, `"planets_page"`, and `"system_page"`.
- `framework/config/env_selection.py`: loads `.env` with `python-dotenv` and selects the target URL from `TEST_ENV`.
- `framework/data/test_data_planet_name.json`: JSON test data containing `planetName`.
- `framework/utils/helpers.py`: helper for loading values from `framework/data/test_data_planet_name.json`.
- `pytest.ini`: pytest and pytest-playwright defaults, Python path, and CLI logging format.
- `requirements.txt`: Python test dependencies.
- `.github/workflows/python-playwright.yml`: GitHub Actions workflow that installs dependencies, installs Chromium, runs `pytest`, and uploads `test-results/*`.
- `.gitignore`: excludes `.env`, `.pytest_cache/`, Python cache files, and Playwright `test-results/` folders.

# Test stack

- Primary test language: Python.
- Test runner: `pytest`.
- Browser automation: Playwright for Python through `pytest-playwright`.
- Assertions: `playwright.sync_api.expect`.
- Configuration/environment loading: `python-dotenv`.
- Test data: JSON loaded with Python `json` from `framework/utils/helpers.py`.
- CI: GitHub Actions on `push` and `pull_request` using Python 3.9 and Chromium.
- Playwright artifacts are configured through pytest options: tracing on, video retained on failure, and screenshots only on failure.

# Test organization and naming conventions

- Test files are in `tests/` and use names ending in `_test.py`.
- Test functions use pytest function naming with the `test_` prefix.
- Existing tests are grouped by UI flow: planet creation in `tests/new_planets_test.py` and spacecraft system checks in `tests/spacecraft_test.py`.
- Page object classes live in `framework/pages/` and are named by page or feature area, such as `BasePage`, `PlanetsPage`, and `SystemChecksPage`.
- Page object files use lowercase snake case names ending in `_page.py`.
- Shared setup for page objects lives in `framework/fixtures/pages_fixture.py`.
- Tests import the `pages` fixture and access page objects from the returned dictionary.
- External test data currently lives in `framework/data/test_data_planet_name.json` and is read through `load_planet_name()`.

# How to run tests

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Chromium:

```bash
python -m playwright install chromium
```

Run all tests:

```bash
pytest
```

Run tests in Chromium:

```bash
pytest --browser=chromium
```

Run in headed mode for local debugging:

```bash
pytest --headed
```

Run a specific test file:

```bash
pytest tests/spacecraft_test.py
```

The repository does not define a coverage command or separate API, integration, or e2e subset commands.

# Configuration and environments

- `pytest.ini` sets default pytest options:

```ini
addopts = --browser=chromium --tracing=on --video=retain-on-failure --screenshot=only-on-failure
```

- `pytest.ini` sets `pythonpath = .`, so tests import project modules from the repository root.
- `pytest.ini` enables CLI logging at `DEBUG` level with timestamp, level, module, function, and message.
- `framework/config/env_selection.py` calls `find_dotenv()` and `load_dotenv()` to load `.env`.
- `TEST_ENV=qa` selects `https://ch-matviy.github.io/space-test-automation-practice-page-qa/`.
- Any other `TEST_ENV` value, or an unset `TEST_ENV`, selects `https://ch-matviy.github.io/space-test-automation-practice-page-dev/`.
- `.env` is ignored by git.
- CI uses `.github/workflows/python-playwright.yml`, installs from `requirements.txt`, installs Chromium, and runs `pytest`.

# HTTP/API client usage

This repository does not contain a dedicated HTTP or API client. The existing automation is browser UI automation through Playwright page objects.

# Required implementation patterns

- Add UI tests under `tests/` using pytest functions with `test_` prefixes.
- Use `framework.config.env_selection.get_url()` for the target URL instead of hardcoding the DEV or QA URL in tests.
- Use `BasePage.navigate(url)` for browser navigation.
- Put reusable selectors and page actions in page object classes under `framework/pages/`.
- Expose new page objects through the `pages` fixture in `framework/fixtures/pages_fixture.py` when tests need them.
- In tests, retrieve page objects from the `pages` fixture dictionary using the existing key style.
- Use Playwright's `expect` assertions against locators for UI assertions.
- Keep reusable JSON test data in `framework/data/` and access it through helper functions in `framework/utils/`.
- Use `logging.info()` for step-level test logging, matching the existing tests.

# Anti-patterns to avoid

- Do not place page locators directly in tests when a page object already owns that page or feature area.
- Do not hardcode the target environment URL in test files; use `get_url()`.
- Do not bypass the `pages` fixture for page object construction in tests.
- Do not commit `.env`, `.pytest_cache/`, or Playwright `test-results/` artifacts.
- Do not use `--headed=false`; the documented usage is to include `--headed` for headed mode or omit it for headless mode.
