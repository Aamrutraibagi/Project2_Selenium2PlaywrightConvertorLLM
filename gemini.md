# Project Constitution: Selenium to Playwright Converter

## Data Schemas

### Input Payload (Selenium Java)
```json
{
  "source_code": "string",
  "framework": "TestNG",
  "language": "Java"
}
```

### Output Payload (Playwright JS/TS)
```json
{
  "converted_code": "string",
  "files": [
    {
      "path": "string",
      "content": "string"
    }
  ],
  "conversion_log": "string"
}
```

## Behavioral Rules
- Priority: Reliability over speed.
- Deterministic business logic for parsing where possible; Ollama for complex logic mapping.
- **Conversion Targets**:
    - Selenium `WebDriver` calls -> Playwright `page` calls.
    - TestNG Annotations (`@Test`, `@BeforeMethod`) -> Playwright Hooks (`test()`, `test.beforeEach()`).
    - Selenium `.findElement().sendKeys()` -> Playwright `page.fill()`.
    - Selenium `.findElement().click()` -> Playwright `page.click()`.
    - Page Object Model: Group actions and selectors into classes.
- **Aesthetics**: Premium UI for code input and side-by-side comparison.
- **Connectivity**: Primary LLM is local Ollama (Endpoint: `http://localhost:11434`).

## Architectural Invariants
- 3-Layer A.N.T. Architecture.
- `tools/` contains Python scripts.
- `architecture/` contains Markdown SOPs.
- `gemini.md` is the Source of Truth/Law.

## Maintenance Log
- **2026-02-08**: Initial V1.1.0 release. 
    - Full conversion logic implementation using local Ollama.
    - Premium UI with Highlight.js and local file storage.
    - Model: `llama3.2` (default).
