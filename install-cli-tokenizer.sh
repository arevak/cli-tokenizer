#!/bin/bash

# Create ~/bin directory if it doesn't exist
mkdir -p ~/bin

# Copy the Python script from current directory
cp ./cli-tokenizer-counter.py ~/bin/cli-tokenizer-counter.py

# Copy the shell wrapper from current directory
cp ./tokens ~/bin/tokens

# Make the shell wrapper executable
chmod +x ~/bin/tokens

echo "Installation complete. Make sure ~/bin is in your PATH, then you can use 'tokens' command."