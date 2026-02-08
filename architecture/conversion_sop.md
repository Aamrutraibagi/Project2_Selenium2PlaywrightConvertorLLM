# SOP: Selenium Java (TestNG) to Playwright (TS) Conversion

## Goal
Transform Selenium Java source code into clean, asynchronous Playwright TypeScript code using the Page Object Model.

## Logic Flow
1. **Extraction Phase**: Use regex/parser to identify Selenium specific calls and TestNG annotations.
2. **LLM Mapping Phase**: Use a deterministic prompt to mapped identified elements to Playwright equivalents.
3. **Structure Phase**: Organize selectors into a POM class and test logic into a separate test file.

## Mapping Rules
| Selenium (Java) | Playwright (TS) | Notes |
| :--- | :--- | :--- |
| `driver.get(url)` | `await page.goto(url)` | |
| `driver.findElement(By.id("foo"))` | `page.locator('#foo')` | |
| `element.sendKeys("bar")` | `await element.fill('bar')` | |
| `element.click()` | `await element.click()` | |
| `@BeforeMethod` | `test.beforeEach(async ({ page }) => { ... })` | |
| `Assert.assertEquals(a, b)` | `expect(a).toBe(b)` | |
