from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from tools.llm_client import LLMClient
from tools.file_handler import FileHandler

# Load environment variables
load_dotenv()

app = Flask(__name__)
llm = LLMClient(provider="ollama")
files = FileHandler(output_dir="converted_tests")

def get_system_prompt():
    sop_path = "architecture/conversion_logic.md"
    if os.path.exists(sop_path):
        with open(sop_path, "r") as f:
            return f.read()
    return "Convert Selenium Java to Playwright TypeScript."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    data = request.json
    java_code = data.get('code', '')
    
    if not java_code:
        return jsonify({"error": "No code provided"}), 400

    # Step 1: Convert using LLM (Layer 3)
    system_prompt = get_system_prompt()
    converted_code = llm.convert_code(java_code, system_prompt)
    
    # Payload Refinement: Strip markdown code blocks if LLM included them
    if "```" in converted_code:
        # Extract content between ```ts or ```javascript or just ```
        import re
        # More robust regex to handle various code block headers
        patterns = [
            r'```(?:typescript|ts|javascript|js|json)?\n([\s\S]*?)\n```',
            r'```([\s\S]*?)```'
        ]
        
        found = False
        for pattern in patterns:
            match = re.search(pattern, converted_code, re.IGNORECASE)
            if match:
                converted_code = match.group(1).strip()
                found = True
                break
        
        if not found:
            converted_code = converted_code.replace("```", "").strip()

    # Step 2: Save to file (Layer 3)
    file_path = files.save_converted_file("converted_test.spec.ts", converted_code)
    
    return jsonify({
        "converted_code": converted_code,
        "file_path": file_path
    })

if __name__ == '__main__':
    app.run(debug=True, port=int(os.getenv("PORT", 5000)))
