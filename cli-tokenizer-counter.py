#!/usr/bin/env python3
import sys
import tiktoken
import argparse

def get_available_encodings():
    # List all available encodings from tiktoken
    return tiktoken.list_encoding_names()

def count_tokens(text, encoding_name="cl100k_base"):
    try:
        encoding = tiktoken.get_encoding(encoding_name)
        return len(encoding.encode(text))
    except KeyError:
        print(f"Error: Encoding '{encoding_name}' not found.")
        print(f"Available encodings: {', '.join(get_available_encodings())}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count tokens in text using different models")
    parser.add_argument("-m", "--model", default="cl100k_base", 
                        help="Encoding model to use (default: cl100k_base)")
    parser.add_argument("-l", "--list", action="store_true",
                        help="List all available encoding models")
    parser.add_argument("text", nargs="*", help="Text to tokenize (optional if piped)")
    
    args = parser.parse_args()
    
    if args.list:
        print("Available encoding models:")
        for encoding in get_available_encodings():
            print(f"  - {encoding}")
        sys.exit(0)
    
    # Get text from arguments or stdin
    if args.text:
        # Text from command line arguments
        text = " ".join(args.text)
    elif not sys.stdin.isatty():
        # Text from stdin
        text = sys.stdin.read().strip()
    else:
        # No input provided
        parser.print_help()
        sys.exit(1)
    
    token_count = count_tokens(text, args.model)
    print(f"Token count ({args.model}): {token_count}")