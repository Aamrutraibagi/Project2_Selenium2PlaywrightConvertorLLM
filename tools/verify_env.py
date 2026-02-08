import sys
import os

def verify():
    print("Python version:", sys.version)
    print("Current Directory:", os.getcwd())
    try:
        import flask
        print("Flask is installed")
    except ImportError:
        print("Flask is NOT installed")
    
    # Check if we can write to .tmp
    if not os.path.exists(".tmp"):
        os.makedirs(".tmp")
    
    with open(".tmp/test.txt", "w") as f:
        f.write("test")
    
    if os.path.exists(".tmp/test.txt"):
        print("File system write verified")
        os.remove(".tmp/test.txt")
    else:
        print("File system write FAILED")

if __name__ == "__main__":
    verify()
