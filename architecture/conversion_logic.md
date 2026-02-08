# SOP: Conversion Logic & Prompt Engineering

## Extraction Logic
The system will identify core Selenium/TestNG components:
- **Selectors**: `By.X`, `findElement`, `findElements`.
- **Actions**: `click()`, `sendKeys()`, `clear()`, `getText()`.
- **Flow**: `@Test`, `@BeforeMethod`, `@AfterMethod`.
- **Assertions**: `Assert.assertTrue`, `Assert.assertEquals`.

## Prompt Engineering Strategy
The LLM prompt must be deterministic and force the output into a specific structure.

### System Prompt Template
```text
You are a Selenium Java to Playwright TypeScript conversion expert.
Rules:
1. Always use async/await.
2. Use Playwright Locators (`page.locator`) instead of `$` or `$$`.
3. Implement the Page Object Model (POM).
4. Extract selectors into a `Page` class.
5. Extract test logic into a `test()` block.
6. Target Language: TypeScript/JavaScript.
7. Assertion Library: Playwright `expect`.
8. STRICT OUTPUT: Return ONLY the code. Do not include explanations, markdown code blocks (```), or preamble. Return raw code ready for execution.
```

### Mapping Matrix (Detailed)
| Category | Selenium/TestNG | Playwright |
| :--- | :--- | :--- |
| Initialization | `WebDriver driver = new ChromeDriver();` | `const { test, expect } = require('@playwright/test');` |
| Navigation | `driver.get("url");` | `await page.goto("url");` |
| Selector (ID) | `By.id("id")` | `page.locator("#id")` |
| Selector (CSS) | `By.cssSelector(".class")` | `page.locator(".class")` |
| Selector (XPath)| `By.xpath("//div")` | `page.locator("//div")` |
| Action | `element.sendKeys("text")` | `await element.fill("text")` |
| Wait | `new WebDriverWait(driver, 10)...` | `await page.waitForSelector(...)` or rely on auto-waiting. |
```
