# alx-frontend-for-fun
Frontend for fun
---

# Description
Markdown is awesome! All your README.md are made in Markdown, but do you know how GitHub are rendering them?

It’s time to code a Markdown to HTML!

# Requirements
```
All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7 or higher)
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the PEP 8 style (version 1.7.*)
All your files must be executable
All your modules should be documented: python3 -c 'print(__import__("my_module").__doc__)'
*Your code should not be executed when imported (by using if __name__ == "__main__":)
```

Tasks
0. Start a script
1. Headings
2. Unordered listing
3. Ordered listing
4. Simple text
5. Bold and emphasis
6. [... but why]()

# Start a script
```
  Write a script markdown2html.py that takes an argument 2 strings:

First argument is the name of the Markdown file
Second argument is the output file name
Requirements:

If the number of arguments is less than 2: print in STDERR Usage: ./markdown2html.py README.md README.html and exit 1
If the Markdown file doesn’t exist: print in STDER Missing <filename> and exit 1
Otherwise, print nothing and exit 0
```

```
guillaume@vagrant:~/$ ./markdown2html.py
Usage: ./markdown2html.py README.md README.html
guillaume@vagrant:~/$ echo $?
1
guillaume@vagrant:~/$
guillaume@vagrant:~/$ ./markdown2html.py README.md README.html 
Missing README.md
guillaume@vagrant:~/$ echo $?
1
guillaume@vagrant:~/$
guillaume@vagrant:~/$ echo "Test" > README.md
guillaume@vagrant:~/$ ./markdown2html.py README.md README.html 
guillaume@vagrant:~/$
```

Repo:

  * GitHub repository: alx-frontend-for-fun
  * File: markdown2html.py

# Headings
Improve markdown2html.py by parsing Headings Markdown syntax for generating HTML:

Syntax: (you can assume it will be strictly this syntax)
<table>
  <th>
    <tr>hello</tr>
  </th>
</table>

  
Markdown	HTML generated
# Heading level 1	<h1>Heading level 1</h1>
## Heading level 2	<h2>Heading level 1</h2>
### Heading level 3	<h3>Heading level 1</h3>
#### Heading level 4	<h4>Heading level 1</h4>
##### Heading level 5	<h5>Heading level 1</h5>
###### Heading level 6	<h6>Heading level 1</h6>
guillaume@vagrant:~/$ cat README.md
# My title
## My title2
# My title3
#### My title4
### My title5

guillaume@vagrant:~/$ ./markdown2html.py README.md README.html 
guillaume@vagrant:~/$ cat README.html 
<h1>My title</h1>
<h2>My title2</h2>
<h1>My title3</h1>
<h4>My title4</h4>
<h3>My title5</h3>
guillaume@vagrant:~/$ 
Spacing and new lines between HTML tags don’t need to be exactly this one

Repo:

GitHub repository: alx-frontend-for-fun
File: markdown2html.py
# Unordered listing
# Ordered listing
# Simple text
# Bold and emphasis
# [... but why]()
