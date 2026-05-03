---
name: web-ui-locators-selector
description: Extract stable web ui locators from the HTML elements passed to the chat and save them as a reusable locator contract.
---

Use this skill when the user selected UI elements in browser and those elements are already present in the chat.

The goal of this skill is to stop repeating the same long prompt every time.

This skill teaches the agent:
- how to read the selected element data
- how to choose the most stable Playwright locator
- how to name elements consistently
- how to organize the locator contract file
- how to flag risky or weak selectors instead of hiding the problem

## Workflow
1. Read the selected browser elements already present in the chat.
2. For each element, extract the best Playwright locator from the available evidence.
3. Prefer locator priority in this order:
   - `getByTestId()`
   - `getByRole()`
   - `getByLabel()`
   - `getByPlaceholder()`
   - `getByText()`
   - CSS/XPath only as a last resort
4. Give each element a clear semantic name like `email_input`, `submit_button`, `error_alert`.
5. Group related elements into one locator contract file for the page or component.
6. For each element, save:
   - purpose
   - locator
   - why it is stable
   - supported action
   - risk notes
7. If multiple locator options exist, choose the most automation-stable one.
8. If the selected element evidence is weak, report the gap instead of inventing a locator.

## Example of the File Content
```md
### email_input
- Purpose: enter the user email
- Locator: page.getByLabel('Email')
- Why stable: label-based locator matches visible form semantics
- Supports action: fill valid or invalid email
- Preconditions: login form is visible
- Risk notes: fails if label text changes

### password_input
- Purpose: enter the password
- Locator: page.getByLabel('Password')
- Why stable: label-based locator matches visible form semantics
- Supports action: fill password
- Preconditions: login form is visible
- Risk notes: none

### submit_button
- Purpose: submit the login form
- Locator: page.getByRole('button', { name: 'Sign in' })
- Why stable: role + accessible name reflects real user behavior
- Supports action: submit login attempt
- Preconditions: form is visible
- Risk notes: duplicated button text elsewhere would make this ambiguous
```
## Guardrails
- Do not invent selectors not supported by the selected elements.
- Do not default to CSS or XPath when semantic locators exist.
- Do not leave the locator list as raw notes. Convert it into a clean reusable contract.
- Do not use random naming. Keep names semantic and consistent.

## Output
Return a clean locator contract file that can be reused later by planning and execution prompts.
