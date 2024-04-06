# Forms
[]() Html, Css && Front-end []()
---

# NEED TO KNOW?
* [An Extensive Guide To Web Form Usability — Smashing Magazine](https://www.smashingmagazine.com/2011/11/extensive-guide-web-form-usability/)
* [Forms - UX Movement](https://uxmovement.com/category/forms/)
* [Placeholders in Form Fields are Harmful (Video)](https://www.nngroup.com/videos/placeholders-form-fields/)
* [The Anatomy of Accessible Forms: Best Practices | Deque](https://www.deque.com/blog/anatomy-of-accessible-forms-best-practices/)
* [Pure CSS Custom Error Messaging for Default Form Elements – Sarah Holley Design](https://sarahholleydesign.com/pure-css-custom-error-messaging-for-default-form-elements/)

MDN resources:

* [HTML forms - Learn web development | MDN](https://developer.mozilla.org/en-US/docs/Learn/Forms)
* [form - HTML: Hypertext Markup Language | MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form)
* [fieldset: The Field Set element - HTML: Hypertext Markup Language | MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/fieldset)
* [legend - HTML: Hypertext Markup Language | MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/legend)
* [label - HTML: Hypertext Markup Language | MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label)
* [input: The Input (Form Input) element - HTML: Hypertext Markup Language | MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input)
* [tabindex - HTML: Hypertext Markup Language | MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/tabindex)
* [accesskey - HTML: Hypertext Markup Language | MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/accesskey)
* [button: The Button element - HTML: Hypertext Markup Language | MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/button)
* [select - HTML: Hypertext Markup Language | MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select)
* [optgroup - HTML: Hypertext Markup Language | MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/optgroup)
* [datalist - HTML: Hypertext Markup Language | MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/datalist)
* [textarea - HTML: Hypertext Markup Language | MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/textarea)
* [Form Validation UX in HTML and CSS | CSS-Tricks](https://css-tricks.com/form-validation-ux-html-css/)
* [Constraint validation - Developer guides | MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Constraint_validation)
* [:invalid - CSS: Cascading Style Sheets | MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/:invalid)
* [:valid - CSS: Cascading Style Sheets | MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/:valid)
* [:optional - CSS: Cascading Style Sheets | MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/:optional)

---


* [How to create an HTML5 form](#how-to-create-an-html5-form)
* [How to choose the right input type](#how-to-choose-the-right-input-type)
* [How to constrain a form field with regular expressions](#how-to-constrain-a-form-field-with-regular-expressions)
* [How to style inputs for invalid, valid, and required fields](#how-to-style-inputs-for-invalid-valid-and-required-fields)
* [How to build a a comment form](#how-to-build-a-a-comment-form)
* [How to build a simple search form](#how-to-build-a-simple-search-form)
* [How to create usable and accessible forms](#how-to-create-usable-and-accessible-forms)

---

# How to create an HTML5 form
     you'll need to use the <form> element along with various input elements for gathering user input. Here's a basic example of an HTML5 form:

```
     <form action="/submit-form" method="post">
    <label for="username">Username:</label>
    <input type="text" id="username" name="username" required>

    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>

    <label for="password">Password:</label>
    <input type="password" id="password" name="password" required>

    <button type="submit">Submit</button>
    </form>

```





---

# How to choose the right input type
    To choose the right input type, you should consider the type of data you're collecting and the user experience you want to provide. Here are some common input types and their uses:
```
    * text: General text input.
    * email: Input for email addresses.
    * password: Input for passwords.
    * number: Input for numbers.
    * date: Input for dates.
    * checkbox: Checkbox for selecting multiple options.
    * radio: Radio buttons for selecting one option from multiple choices.
```
# How to constrain a form field with regular expressions

    To constrain a form field with regular expressions, you can use the pattern attribute along with a regular expression.

Example:
```
    <input type="text" pattern="[A-Za-z]{3}" title="Three letter word">

```
# How to style inputs for invalid, valid, and required fields
This input field only accepts three-letter words.

To style inputs for invalid, valid, and required fields, you can use the :valid, :invalid, and :required CSS pseudo-classes, respectively. 

Example:
```
    input:valid {
        border-color: green;
    }

    input:invalid {
        border-color: red;
    }

    input:required {
        background-color: yellow;
    }

```
# How to build a a comment form
To build a comment form, you can follow a similar structure as the basic form above.

Example:
```
    <form action="/submit-comment" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="comment">Comment:</label>
        <textarea id="comment" name="comment" required></textarea>

        <button type="submit">Submit</button>
    </form>
```
# How to build a simple search form
To build a simple search form, you can use the <code><input type="search"></code> element:

```<form action="/search" method="get">
        <label for="search">Search:</label>
        <input type="search" id="search" name="q" required>

        <button type="submit">Search</button>
    </form>

```
# How to create usable and accessible forms

To create usable and accessible forms, consider the following tips:
```
    * Use clear and descriptive labels for each input field.
    
    * Provide helpful error messages for invalid input.
    
    * Ensure that the form can be navigated and submitted using only the keyboard.
    
    * Use HTML5 form validation and provide additional client-side validation if needed.
    
    * Test your forms with real users to identify any usability issues.
    
    * Follow accessibility best practices, such as using proper markup, providing alternative text for images, and ensuring adequate color contrast.
    
    * Use ARIA roles and attributes to improve accessibility for screen reader users.
```









---

[`^`](#need-to-know)

---