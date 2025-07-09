def is_palindrome():
    import sys
    import re

    # Read input string from stdin
    s = sys.stdin.read().strip()

    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

    # Check if the cleaned string is a palindrome
    if cleaned == cleaned[::-1]:
        print("True")
    else:
        print("False")
