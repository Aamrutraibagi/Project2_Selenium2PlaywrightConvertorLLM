# UI Design System: Selenium to Playwright Converter

## Aesthetics
- **Theme**: Dark Mode (Slate/Zinc).
- **Primary Color**: Indigo/Blue.
- **Font**: Inter/Roboto.
- **Components**:
    - **Header**: Clean title with "B.L.A.S.T. Converter" branding.
    - **Input Section**: Large CodeMirror or standard text area for Java code.
    - **Output Section**: Resizable side-by-side view (Java vs. TS).
    - **Controls**: "Convert" button with loading state, "Copy" button for the result.
    - **Status Bar**: Progress feedback (Connecting LLM -> Parsing -> Finalizing).

## Tech Stack
- **Framework**: Flask (Backend).
- **Styling**: TailwindCSS via CDN (for ease of local execution without build steps).
- **Interactivity**: Vanilla JavaScript (AJAX/Fetch).

## Layout
```text
+-------------------------------------------------+
|                  B.L.A.S.T. Converter           |
+-------------------------------------------------+
| [ Java Input ]             | [ TS Output ]      |
|                            |                    |
|                            |                    |
| (Paste Java Here)          | (Result Here)      |
+-------------------------------------------------+
| [ Convert Button ]                              |
+-------------------------------------------------+
```
