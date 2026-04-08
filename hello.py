def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("World"))
EOFPart E — Explore GitHub Issues
Go to your repository on GitHub and click the Issues tab. Create a new issue:

Title: Add a farewell function to hello.py
Body: The greet() function says hello. We should also add a farewell() function that says goodbye.
Add the label enhancement (create it if it does not exist)
Assign it to yourself
Note the issue number (it will be #1). Now implement the fix in a new branch:

git checkout -b feature/farewell
Edit hello.py:

cat >> hello.py << 'EOF'

def farewell(name):
    """Return a farewell string."""
    return f"Goodbye, {name}! Thanks for using GitHub Cloud."

if __name__ == "__main__":
    print(farewell("World"))
