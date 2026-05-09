# IBM Full Stack Software Developer

<span class="track-badge fullstack">Web Foundation Track</span>

## What This Covers

The local materials for this track currently cover the course "Introduction to HTML, CSS, & JavaScript," with modules on basic HTML and common HTML5 structural and form elements.

## Core Ideas

- HTML gives a page semantic structure.
- CSS controls visual presentation.
- JavaScript adds behavior and interactivity.
- Semantic tags make pages easier for browsers, screen readers, and developers to understand.
- Forms collect user input, and field grouping improves clarity.

## Important Formulas

There are no mathematical formulas in the local HTML materials. The core structure is hierarchical rather than numeric:

\[
\text{web page} = \text{semantic structure} + \text{presentation} + \text{behavior}
\]

Where:

- Semantic structure is HTML.
- Presentation is CSS.
- Behavior is JavaScript.

## Explanation

This track introduces the browser as an application platform. HTML is the foundation because it describes what the content means. CSS changes how that content looks. JavaScript responds to user actions and updates the page.

The available modules emphasize HTML structure: headings, paragraphs, lists, links, images, forms, and newer HTML5 semantic elements such as `header`, `nav`, `main`, `section`, `article`, and `footer`.

## Key Code Patterns

Basic page structure:

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Example Page</title>
  </head>
  <body>
    <main>
      <h1>Page title</h1>
      <p>Page content.</p>
    </main>
  </body>
</html>
```

## Detailed Study Notes

HTML, CSS, and JavaScript are separate layers. HTML describes meaning and structure. CSS describes appearance. JavaScript describes behavior. Keeping those responsibilities separate makes pages easier to maintain because changing the color of a button should not require rewriting the form markup, and validating a form should not require changing the page hierarchy.

Semantic HTML gives names to regions of the page:

```html
<header>Introductory content</header>
<nav>Navigation links</nav>
<main>Primary page content</main>
<aside>Related supporting content</aside>
<footer>Closing page information</footer>
```

Forms should connect labels to inputs. This improves click targets, screen reader output, and general clarity:

```html
<label for="email">Email address</label>
<input id="email" name="email" type="email" required>
```

CSS and JavaScript can then target meaningful elements without destroying structure:

```css
main {
  max-width: 72rem;
  margin: 0 auto;
}
```

```javascript
document.querySelector("form").addEventListener("submit", handleSubmit);
```

## Common Mistakes

- Choosing tags only for appearance instead of meaning.
- Skipping labels for form controls.
- Using too many generic `div` elements where semantic tags would be clearer.
- Forgetting that assistive technologies rely on the document structure.

## Takeaways

The current full-stack materials establish HTML fundamentals. Good frontend work starts with meaningful structure before styling or scripting.
