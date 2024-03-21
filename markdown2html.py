#!/usr/bin/python3
"""
Converts a Markdown file to HTML
parsing headings,
unordered,
and ordered list syntax,
paragraph syntax,
and bold syntax with special formatting rules.
"""

import sys
import os.path
import re
import hashlib


def convert_markdown_to_html(markdown_file, output_file):
    """
    Converts a Markdown file to HTML, parsing headings,
    unordered, and ordered list syntax, paragraph syntax,
    and bold syntax with special formatting rules.

    Args:
        markdown_file (str): The name of the Markdown file.
        output_file (str): The name of the output HTML file.
    """
    if not os.path.isfile(markdown_file):
        # Check if the Markdown file exists
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Dictionary to map Markdown heading levels to HTML tags
    heading_mapping = {
        '#': 'h1',
        '##': 'h2',
        '###': 'h3',
        '####': 'h4',
        '#####': 'h5',
        '######': 'h6'
    }

    # Dictionary to map Markdown list characters to HTML tags
    list_mapping = {
        '*': 'ul',
        '1.': 'ol'
    }

    # Regular expression pattern to match ordered list syntax
    ordered_list_pattern = re.compile(r'^\d+\.')

    # Regular expression pattern to match bold syntax
    bold_pattern = re.compile(r'\*\*(.*?)\*\*')

    # Regular expression pattern to match special formatting syntax
    special_format_pattern = re.compile(r'\[\[(.*?)\]\]|\(\((.*?)\)\)')

    # Read the contents of the Markdown file
    with open(markdown_file, 'r') as f:
        lines = f.readlines()

    html_lines = []
    in_list = False
    in_paragraph = False
    for line in lines:
        line = line.strip()
        if line.startswith('#'):
            # Extract heading level and text
            heading_level, heading_text = line.split(' ', 1)
            html_tag = heading_mapping.get(heading_level, 'h1')
            html_lines.append(f"<{html_tag}>{heading_text}</{html_tag}>")
        elif line.startswith('- ') or ordered_list_pattern.match(line):
            list_char = line[0]
            # Get the first character of the line
            list_tag = list_mapping.get(list_char, 'ul')
            # Map list character to HTML tag
            if not in_list:
                html_lines.append(f'<{list_tag}>')
                in_list = True
            if ordered_list_pattern.match(line):
                # For ordered lists, remove the numbers and dot from the line
                line = line.replace(re.search(r'^\d+\.', line).group(), '')
            list_item_text = line[2:] if list_char == '*' else line[3:]
            # Remove list character from text
            html_lines.append(f"<li>{list_item_text.strip()}</li>")
        elif line:
            if in_list:
                html_lines.append(f'</{list_tag}>')
                in_list = False
            if not in_paragraph:
                html_lines.append('<p>')
                in_paragraph = True

            # Replace bold syntax with HTML tags
            line = bold_pattern.sub(r'<b>\1</b>', line)

            # Apply special formatting rules
            line = special_format_pattern.sub(
                lambda m: hashlib.md5(m.group(1).lower().encode()).hexdigest()
                if m.group(1) else m.group(2).replace('c', '', -1).title(),
                line
            )

            html_lines.append(line)
        else:
            if in_list:
                html_lines.append(f'</{list_tag}>')
                in_list = False
            if in_paragraph:
                html_lines.append('</p>')
                in_paragraph = False

    # If a list is still open, close it
    if in_list:
        html_lines.append(f'</{list_tag}>')
    # If a paragraph is still open, close it
    if in_paragraph:
        html_lines.append('</p>')

    # Write HTML output to the specified file
    with open(output_file, 'w') as f:
        f.write('\n'.join(html_lines))

    print("Conversion successful!")
    sys.exit(0)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        # Check if correct number of arguments is provided
        print(
            "Usage: ./markdown2html.py README.md README.html",
            file=sys.stderr
        )
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_markdown_to_html(markdown_file, output_file)
