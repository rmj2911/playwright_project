# Playwright Python Automation Framework

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Playwright](https://img.shields.io/badge/Playwright-Python-green)
![pytest](https://img.shields.io/badge/Test%20Runner-pytest-orange)

This project is a portfolio-ready UI test automation framework built with Python, pytest, and Playwright. It validates key user flows on the Space Test Automation Practice page using a clean Page Object Model structure, reusable fixtures, external test data, and GitHub Actions CI.

## Project Highlights

- Built with `pytest-playwright` for browser automation and assertions.
- Uses the Page Object Model to keep selectors and page actions organized.
- Supports environment-based URL selection with `python-dotenv`.
- Stores test data separately in JSON for easier maintenance.
- Runs automatically in GitHub Actions on push and pull request events.
- Captures Playwright traces, videos, and screenshots for failed test debugging.

## Test Coverage

The suite currently validates:

- Adding a new planet and confirming the success message.
- Selecting all spacecraft system checks and verifying the "All Systems Go" state.
- Unchecking propulsion and verifying the "Systems Pending" state.

## Tech Stack

- Python 3.9
- [pytest](https://docs.pytest.org/)
- [Playwright for Python](https://playwright.dev/python/)
- [pytest-playwright](https://github.com/microsoft/playwright-pytest)
- [python-dotenv](https://github.com/theskumar/python-dotenv)

## Automation Approach

This framework separates test intent from page implementation details:

- Tests in `tests/` describe user behavior and expected outcomes.
- Page objects in `framework/pages/` contain locators and page actions.
- Fixtures in `framework/fixtures/` provide reusable page object instances.
- Config in `framework/config/` selects the target environment.
- Data in `framework/data/` keeps test input separate from test logic.

## Project Structure

```text
.
├── .github/workflows/              # GitHub Actions workflow
├── framework/
│   ├── config/env_selection.py     # Env-based URL selection
│   ├── data/test_data_planet_name.json
│   ├── fixtures/pages_fixture.py   # Page object fixture mapping
│   ├── pages/                      # Page Object Model classes
│   └── utils/helpers.py            # Test data helper
├── tests/
│   ├── new_planets_test.py
│   └── spacecraft_test.py
├── pytest.ini
└── requirements.txt
```

## Prerequisites

- Python 3.9 or higher
- `pip` available
- Git installed

## Local Setup

1. Clone the repo:

   ```bash
   git clone https://github.com/rmj2911/playwright_project.git
   cd playwright_project
   ```

2. Create and activate a virtual environment:

   macOS/Linux:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   Windows (PowerShell):
   ```powershell
   py -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Install Playwright browser (Chromium):

   ```bash
   python -m playwright install chromium
   ```

## Running Tests

Run all tests:

```bash
pytest
```

Run tests in Chromium:

```bash
pytest --browser=chromium
```

Run in headed mode (local debugging):

```bash
pytest --headed
```

Run specific test file:

```bash
pytest tests/spacecraft_test.py
```

The default configuration is managed in `pytest.ini`:

```ini
addopts = --browser=chromium --tracing=on --video=retain-on-failure --screenshot=only-on-failure
```

## Environment Selection

Target URL is selected in `framework/config/env_selection.py`:

- `TEST_ENV=qa` -> QA URL
- any other value (or unset) -> DEV URL (default)

Optional `.env` file example:

```env
TEST_ENV=qa
```

## CI with GitHub Actions

Workflow file: `.github/workflows/python-playwright.yml`

The workflow:

- Runs on `push` and `pull_request`
- Sets up Python 3.9
- Installs dependencies and Chromium
- Runs `pytest`
- Uploads artifacts from `test-results/*`

## Key Files

- `tests/new_planets_test.py`: validates adding a planet.
- `tests/spacecraft_test.py`: validates spacecraft system checkbox behavior.
- `framework/pages/planets_page.py`: page object for planet form interactions.
- `framework/pages/system_checks_page.py`: page object for system check interactions.
- `framework/fixtures/pages_fixture.py`: shared fixture that exposes page objects to tests.
- `pytest.ini`: pytest and Playwright runtime options.

## Troubleshooting

### Error: "Missing X server or $DISPLAY" in CI

This means tests are trying to run in headed mode on a headless Linux runner.

Use default headless mode in CI and avoid adding `--headed`.

If you need headed execution in Linux CI, run tests with `xvfb-run`.

### Error: `pytest: argument --headed: ignored explicit argument 'false'`

Do not use `--headed=false`.  
`--headed` is a boolean flag:

- include `--headed` to force headed mode
- omit `--headed` to run headless

### Node.js deprecation warning in Actions

If Actions warns about Node 20, keep action versions current and optionally set:

```yaml
env:
  FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true
```

## Repository

GitHub: [rmj2911/playwright_project](https://github.com/rmj2911/playwright_project)
