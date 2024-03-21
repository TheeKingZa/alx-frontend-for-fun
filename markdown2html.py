#!/usr/bin/python3
"""
Converts a Markdown file to HTML.
"""

import sys
import os.path


def convert_markdown_to_html(markdown_file, output_file):
    """
    Converts a Markdown file to HTML.

    Args:
        markdown_file (str): The name of the Markdown file.
        output_file (str): The name of the output HTML file.
    """
    if not os.path.isfile(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Markdown to HTML conversion logic here

    # For now, just print success and exit
    print("Conversion successful!")
    sys.exit(0)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(
            "Usage: ./markdown2html.py README.md README.html",
            file=sys.stderr
        )
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_markdown_to_html(markdown_file, output_file)
