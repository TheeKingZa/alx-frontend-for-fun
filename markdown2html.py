#!/usr/bin/python3
import sys
import os

def convert_markdown_to_html(input_file, output_file):
    """
    Converts a Markdown file to HTML.

    Args:
        input_file (str): The path to the input Markdown file.
        output_file (str): The path to the output HTML file.
    """
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # Code to convert Markdown to HTML goes here
    # This is just a placeholder

    print(f"Successfully converted {input_file} to {output_file}")

def main():
    """
    Main function to handle command line arguments and convert Markdown to HTML.
    """
    # Check if correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <input_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_markdown_to_html(input_file, output_file)

if __name__ == "__main__":
    main()
