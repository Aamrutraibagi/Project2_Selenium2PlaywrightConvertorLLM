import os
import requests
from dotenv import load_dotenv

# Load env in case this is run standalone
load_dotenv()

class LLMClient:
    def __init__(self, provider="ollama"):
        self.provider = provider
        self.base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        self.model = os.getenv("OLLAMA_MODEL", "codellama")

    def convert_code(self, source_code, system_prompt):
        """
        Calls Ollama Chat API to convert Selenium Java to Playwright TS.
        """
        try:
            response = requests.post(
                f"{self.base_url}/api/chat",
                json={
                    "model": self.model,
                    "messages": [
                        {
                            "role": "system",
                            "content": system_prompt
                        },
                        {
                            "role": "user",
                            "content": f"Convert this Selenium Java code to Playwright TypeScript:\n\n{source_code}"
                        }
                    ],
                    "stream": False
                },
                timeout=150
            )
            if response.status_code != 200:
                return f"// ERROR: Ollama returned {response.status_code}: {response.text}"
            
            result = response.json()
            message = result.get("message", {})
            return message.get("content", "// ERROR: No response content from Ollama")
        except Exception as e:
            return f"// ERROR: Ollama chat failed: {str(e)}"

if __name__ == "__main__":
    # Test client
    client = LLMClient()
    sample_code = """
    WebDriver driver = new ChromeDriver();
    driver.get("https://google.com");
    driver.quit();
    """
    print(client.convert_code(sample_code, "Convert to Playwright TypeScript."))
