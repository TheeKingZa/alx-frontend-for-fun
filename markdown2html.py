#!/usr/bin/python3
"""
Converts a Markdown file to HTML, parsing headings and unordered list syntax.
"""

import sys
import os.path


def convert_markdown_to_html(markdown_file, output_file):
    """
    Converts a Markdown file to HTML, parsing headings
    and unordered list syntax.

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

    # Read the contents of the Markdown file
    with open(markdown_file, 'r') as f:
        lines = f.readlines()

    html_lines = []
    in_list = False
    for line in lines:
        line = line.strip()
        if line.startswith('#'):
            # Extract heading level and text
            heading_level, heading_text = line.split(' ', 1)
            html_tag = heading_mapping.get(heading_level, 'h1')
            # Map Markdown heading level to HTML tag
            html_lines.append(f"<{html_tag}>{heading_text}</{html_tag}>")
            # Generate HTML line with corresponding tag
        elif line.startswith('- '):
            if not in_list:
                html_lines.append('<ul>')
                # Start unordered list
                in_list = True
            # Extract list item text and add to HTML
            list_item_text = line[2:]
            html_lines.append(f"<li>{list_item_text}</li>")
        else:
            if in_list:
                html_lines.append('</ul>')
                # End unordered list if no more list items
                in_list = False
            html_lines.append(line)
            # If not a heading or list item, simply append the line

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
