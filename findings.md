# Research & Findings
- Project Name: Selenium to Playwright (JS/TS) Converter
- Protocol: B.L.A.S.T.
- Tech Stack: Python (Backend), HTML5/TailwindCSS (Frontend), Ollama (Local LLM: codellama)

## Discoveries
- **North Star**: Selenium Java to Playwright (JS/TS) Converter.
- **Integrations**: TestNG Selenium Java tests to Playwright JS/TS.
- **Source of Truth**: User manual input via a UI.
- **Delivery Payload**: Converted code saved to a new local directory and displayed in the UI.
- **Behavioral Rules**: 
    - Full conversion including Page Object Model (POM).
    - Use specific assertion libraries (Playwright built-in).
    - Maintain existing wait times (map Selenium waits to Playwright waits).

## Research Findings
- **Conversion Strategy**: Direct line-by-line translation is insufficient; must handle the async/await shift and Playwright's auto-waiting.
- **Mapping Table**:
  - `driver.get(url)` -> `await page.goto(url)`
  - `driver.findElement(By.id(id))` -> `page.locator('#id')`
  - `@Test` -> `test('name', async ({ page }) => { ... })`
  - `driver.quit()` -> No direct equivalent in test scope; handled by Playwright runner.
- **POM Implementation**: Requires extracting element definitions into separate classes with clear interaction methods.
