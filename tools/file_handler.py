import os

class FileHandler:
    def __init__(self, output_dir="output"):
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def save_converted_file(self, filename, content):
        """
        Saves the converted code to the local output directory.
        """
        file_path = os.path.join(self.output_dir, filename)
        with open(file_path, "w") as f:
            f.write(content)
        return file_path

if __name__ == "__main__":
    handler = FileHandler()
    print(handler.save_converted_file("test.spec.ts", "// Playwright code"))
