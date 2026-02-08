# B.L.A.S.T. Selenium to Playwright Converter (Local LLM) 🚀

An intelligent, deterministic, and self-healing automation converter that transforms **Selenium Java (TestNG)** code into high-quality **Playwright TypeScript/JavaScript** using local LLM power via Ollama.

![Project Screenshot](demo_screenshot.png)

## ✨ Features
- **Intelligent Mapping**: Converts `WebDriver` actions, TestNG annotations, and assertions to their Playwright equivalents.
- **Page Object Model (POM)**: Automatically extracts selectors and actions into a clean POM structure.
- **Premium UI**: Sleek, dark-mode interface with side-by-side code blocks and syntax highlighting.
- **Local LLM Integration**: Uses **Ollama** (`llama3.2` or `codellama`) to ensure your test code stays private and local.
- **One-Click Actions**: Easily **Copy** to clipboard or **Download** the converted `.spec.ts` file.

## 🏗️ Architecture (A.N.T.)
This project follows the **A.N.T. 3-Layer Architecture**:
1. **Layer 1 (Architecture)**: Markdown-based SOPs defining the technical conversion rules.
2. **Layer 2 (Navigation)**: Flask-based routing layer orchestrating UI and Tools.
3. **Layer 3 (Tools)**: Deterministic Python scripts for LLM interaction and file handling.

## 🚀 Getting Started

### Prerequisites
1. **Python 3.10+**
2. **Ollama** installed and running (`ollama serve`).
3. **Llama3.2** model pulled:
   ```bash
   ollama pull llama3.2
   ```

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Aamrutraibagi/Project2_Selenium2PlaywrightConvertorLLM.git
   cd Project2_Selenium2PlaywrightConvertorLLM
   ```
2. Install dependencies:
   ```bash
   pip install flask python-dotenv requests
   ```
3. Initialize the environment:
   ```bash
   cp .env.example .env
   ```

### Running the App
1. Start the Flask server:
   ```bash
   python3 app.py
   ```
2. Open your browser to: `http://localhost:5000`
3. Paste your Selenium Java code and click **Convert**.

## 🛠️ Configuration
Edit the `.env` file to customize the Ollama endpoint or model:
```env
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2
```

## 📜 License
MIT License - Created by [Amrut Raibagi](https://github.com/Aamrutraibagi)
