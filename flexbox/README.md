# Flexbox
`HTML`, `CSS` and `Front-end`
---

`Read` or `watch`:
* [A Complete Guide to Flexbox | CSS-Tricks](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
* [Flexbox Froggy - A game for learning CSS flexbox](https://flexboxfroggy.com/)
* [Flexbox Defense](http://www.flexboxdefense.com/)
* [Flexbox Cheatsheet](https://yoksel.github.io/flex-cheatsheet/)
* [CSS Flexible Box Layout - CSS: Cascading Style Sheets | MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout)
* [afonsopacifer/awesome-flexbox: A curated list of CSS Flexible Box Layout Module or only Flexbox.](https://github.com/afonsopacifer/awesome-flexbox)
* [Build with Flexbox](https://flexbox.buildwithreact.com/)
* [Flexplorer](https://bennettfeely.com/flexplorer/)
* [CSS Flexible Box Layout Module Level 1](https://www.w3.org/TR/css-flexbox-1/#flex)
* [FLEX: A simple visual cheatsheet for flexbox](https://flexbox.malven.co/)


# NEED TO KNOW!?
* [What is Flexbox?](#what-is-flexbox)
* [How to convert float positioning to a flex display](#how-to-convert-float-positioning-to-a-flex-display)
* [How to horizontally and vertically align elements using Flexbox](#how-to-horizontally-and-vertically-align-elements-using-flexbox)
* [The difference between the main and cross axes](#the-difference-between-the-main-and-cross-axes)
* [Properties that work on flex elements vs flex container](#properties-that-work-on-flex-elements-vs-flex-container)
* [Shorthands for flex](#shorthands-for-flex)
* [How to create a new page with flex in mind](#how-to-create-a-new-page-with-flex-in-mind)

---


# What is Flexbox?

Flexbox, or the Flexible Box Layout, is a layout model in CSS designed for creating efficient and flexible layouts in web applications. It provides a more efficient way to distribute space and align items within a container, even when their size is unknown or dynamic. Flexbox introduces a set of CSS properties that control the layout, alignment, and distribution of items within a flex container.

---

[`^`](#need-to-know)

---
# How to convert float positioning to a flex display

To convert float positioning to a flex display, follow these steps:

Change the display property of the container to display: flex;.
Remove any floats from the child elements.
Use flex properties such as flex-direction, justify-content, and align-items to control the layout and alignment of the flex items.

Example:

```
    .container {
    display: flex;
    flex-direction: row; /* or column, depending on your layout */
    justify-content: space-between; /* or other alignment options */
    align-items: center; /* or other alignment options */
    }

    .child {
    /* Remove float properties */
    }
```

---

[`^`](#need-to-know)

---
# How to horizontally and vertically align elements using Flexbox

To horizontally and vertically align elements using Flexbox:

Use justify-content to align items along the main axis (horizontally).
Use align-items to align items along the cross axis (vertically).
Use align-self on individual items to override the alignment for specific items.
Example:
```
    .container {
    display: flex;
    justify-content: center; /* Horizontally center items */
    align-items: center; /* Vertically center items */
    }

    .child {
    align-self: flex-end; /* Align this item to the end of the cross axis */
    }
```
---

[`^`](#need-to-know)

---
# The difference between the main and cross axes

    * The main axis is the primary axis along which flex items are laid out. It's defined by the flex-direction property.
    * The cross axis is perpendicular to the main axis. Its direction depends on the flex-direction property.

---

[`^`](#need-to-know)

---
# Properties that work on flex elements vs flex container

    * Properties that work on flex elements (flex items) include order, flex-grow, flex-shrink, flex-basis, align-self, etc.
    
    * Properties that work on the flex container include display, flex-direction, justify-content, align-items, align-content, etc.

---

[`^`](#need-to-know)

---
# Shorthands for flex

    * The shorthand property for setting flex-grow, flex-shrink, and flex-basis is flex.
    * For example: 
    ```
    flex: 1 1 auto;
    ```
    is equivalent to 
    ```
    flex-grow: 1;
    flex-shrink: 1;
    flex-basis: auto;
    ```

---

[`^`](#need-to-know)

---
# How to create a new page with flex in mind

To create a new page with Flexbox in mind:

* Design your layout structure using flex containers and flex items.
* Use appropriate flex properties to control the layout, alignment, and distribution of items within containers.
* Test the layout across different screen sizes and devices to ensure responsiveness.
* Use media queries to adjust the layout for specific viewport sizes if necessary.
* Consider browser compatibility and provide fallbacks or alternative layouts for older browsers if needed.

Example:

html
```
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flexbox Page</title>
    <link rel="stylesheet" href="styles.css">
    </head>
    <body>
    <div class="container">
        <div class="item">Item 1</div>
        <div class="item">Item 2</div>
        <div class="item">Item 3</div>
    </div>
    </body>
    </html>
```
css
```
    .container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    }

    .item {
    padding: 20px;
    border: 1px solid #ccc;
    margin: 10px;
    }
```

This creates a simple page with three flex items horizontally centered and vertically aligned in the viewport. Adjust styles and properties as needed to create the desired layout.

---

[`^`](#need-to-know)

---