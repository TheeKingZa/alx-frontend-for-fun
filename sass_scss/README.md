# Sass & Scss
---

`Read` or `watch`:
* [Sass Basics](https://sass-lang.com/guide/)
* [Sass flow control directives: @if, @for, @each and @while](https://sass-lang.com/documentation/at-rules/control/)
* [Sass references](https://sass-lang.com/documentation/)

# NEED TO KNOW?
* [What Sass means](#what-sass-means)
* [How to write Sass & Scss file](#how-to-write-sass--scss-file)
* [What is the difference between Sass and Scss](#difference-between-sass-and-scss)
* [What is the Sass preprocessing](#sass-preprocessing)
* [How to declare a variable](#how-to-declare-a-variable)
* [How to use nested definition](#how-to-use-nested-definition)
* [How to import a Sass file](#how-to-import-a-sass-file)
* [How to use mixins](#how-to-use-mixins)
* [How to declare extend/inheritance styles](#how-to-declare-extendinheritance-styles)
* [How to manipulate operators](#how-to-manipulate-operators)
---

# Getting Started with Scss
Comments for your Scss file:
    * All your Scss file must start with a comment block
```
    $ cat my_styles.scss
    /* My style */
    body {
        .container {
            color: #3D3D3D;
        }
    }
    $

```

# Install Sass/Scss on Ubuntu 18.04 LTS
```
    $ sudo apt-get install -y ruby2.5 ruby2.5-dev
    $ sudo apt-get install ubuntu-dev-tools
    $ gem install sass -v 3.7.4
    $ sass --version
    Ruby Sass 3.7.4
```

---
# What Sass means:
Sass stands for "Syntactically Awesome StyleSheets". It's a preprocessor scripting language that is interpreted or compiled into Cascading Style Sheets (CSS).
---

[`^`](#need-to-know)

---
# How to write Sass & Scss file:
Sass files can have either the .sass or .scss extension. .sass uses indentation to separate code blocks, while .scss uses curly braces and semicolons, similar to CSS.

```
sass
----
    // Example of Sass file
    $primary-color: #333

    body
    font-family: Arial, sans-serif
    color: $primary-color

scss
----
    // Example of SCSS file
    $primary-color: #333;

    body {
    font-family: Arial, sans-serif;
    color: $primary-color;
    }

```
---

[`^`](#need-to-know)

---
# Difference between Sass and Scss:
    ```
    The main difference between Sass and SCSS lies in their syntax. Sass uses indentation for nesting and omits semicolons and braces, while SCSS uses braces, semicolons, and a CSS-like syntax. Otherwise, they offer the same features and functionality.
    ```
---

[`^`](#need-to-know)

---
# Sass preprocessing:
Sass preprocessing is the process of converting Sass or SCSS code into CSS. This is typically done using a preprocessor like Dart Sass, Node Sass, or Ruby Sass.

# How to declare a variable:
Variables in Sass are declared using the $ symbol followed by the variable name and its value.
```
scss
----
    $primary-color: #333;

```
---

[`^`](#need-to-know)

---
# How to use nested definition:
Sass allows for nested CSS rules, which helps to organize and clarify your styles.
```
scss
----
    nav {
    ul {
        margin: 0;
        padding: 0;
        list-style: none;
    }

    li {
        display: inline-block;
        margin-right: 10px;
    }

    a {
        text-decoration: none;
        color: $primary-color;
    }
    }

```
---

[`^`](#need-to-know)

---
# How to import a Sass file:
Sass files can be imported using the @import directive.
```
scss
----
    @import 'variables';

```
---

[`^`](#need-to-know)

---
# How to use mixins:
Mixins in Sass are reusable blocks of styles that can be included in other rules using the @include directive.

```
scss
----

    @mixin border-radius($radius) {
    border-radius: $radius;
    }

    .box {
    @include border-radius(10px);
    }

```
---

[`^`](#need-to-know)

---
# How to declare extend/inheritance styles:
In Sass, you can use @extend to inherit styles from one selector to another.

```
scss
----
    .btn {
    padding: 10px 20px;
    background-color: #333;
    color: white;
    }

    .btn-primary {
    @extend .btn;
    background-color: blue;
    }

```
---

[`^`](#need-to-know)

---
# How to manipulate operators:
Sass supports various mathematical operators such as `+`, `-`, `*`, `/`, and `%`, which can be used to manipulate values in calculations.
```
scss
----
    $width: 100px;
    $padding: 20px;

    .box {
    width: $width + $padding;
    }

```

---

These are the basics of Sass that cover a range of topics from syntax to advanced features like mixins and inheritance. Let me know if you need further clarification on any of these points!

---

[`^`](#need-to-know)
[`GettingStarted`](#getting-started-with-scss)
---
