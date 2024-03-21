#!/usr/bin/python3
"""Markdown to HTML Converter"""

import sys
import os
import re
import hashlib


def print_usage():
    """Prints script usage"""
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)


def parse_headings(line):
    """Parse headings syntax"""
    # Check for headings syntax and replace with HTML tags
    match = re.match(r'^(#+)\s(.*)', line)
    if match:
        level = len(match.group(1))
        title = match.group(2)
        return f"<h{level}>{title}</h{level}>"
    return line


def parse_listings(line):
    """Parse listings syntax"""
    # Check for unordered listing syntax and replace with HTML tags
    if re.match(r'^\s*-\s(.*)', line):
        return "<li>" + line.strip()[2:] + "</li>"

    # Check for ordered listing syntax and replace with HTML tags
    if re.match(r'^\s*\*\s(.*)', line):
        return "<li>" + line.strip()[2:] + "</li>"

    return line


def parse_paragraph(line):
    """Parse paragraph syntax"""
    # Check for empty line and return empty string
    if line.strip() == "":
        return ""

    # Check for simple text and replace with HTML tags
    return f"<p>\n    {line.strip()}\n</p>\n"


def parse_bold_and_emphasis(line):
    """Parse bold and emphasis text syntax"""
    # Replace **bold** with <b>bold</b>
    line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)
    # Replace __emphasis__ with <em>emphasis</em>
    line = re.sub(r'__(.*?)__', r'<em>\1</em>', line)
    return line


def parse_special_syntax(line):
    """Parse special syntax"""
    # Replace [[Hello]] with MD5 hash of "Hello"
    line = re.sub(
        r'\[\[(.*?)\]\]',
        lambda match: hashlib.md5(match.group(1).encode()).hexdigest(),
        line
    )
    # Remove all occurrences of 'c' (case insensitive) from ((Hello Chicago))
    line = re.sub(
        r'\(\((.*?)\)\)',
        lambda match: match.group(1).replace('c', '').replace('C', ''),
        line
    )
    return line


def convert_markdown_to_html(markdown_file, output_file):
    """Convert Markdown to HTML"""
    with open(markdown_file, 'r') as f:
        lines = f.readlines()

    # Parse each line and write to output file
    with open(output_file, 'w') as f:
        for line in lines:
            line = parse_headings(line)
            line = parse_listings(line)
            line = parse_paragraph(line)
            line = parse_bold_and_emphasis(line)
            line = parse_special_syntax(line)
            f.write(line)


def main():
    """Main function"""
    # Check number of arguments
    if len(sys.argv) != 3:
        print_usage()
        sys.exit(1)

    # Get input and output file names
    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if markdown file exists
    if not os.path.isfile(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Convert markdown to HTML
    convert_markdown_to_html(markdown_file, output_file)

    # Exit with success code
    sys.exit(0)


if __name__ == "__main__":
    main()
