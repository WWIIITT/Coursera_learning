# HTML, CSS, and JavaScript - Module 1

<span class="track-badge fullstack">IBM Full Stack Software Developer</span>

## What This Covers

Module 1 introduces HTML through a hands-on JSFiddle lab. The focus is writing basic page content and understanding how HTML tags structure text and media in a browser.

## Core Ideas

- HTML documents are made of nested elements.
- Headings create document hierarchy.
- Paragraphs, links, images, and lists express common content types.
- Attributes provide extra information such as link targets or image sources.
- Browser-based tools like JSFiddle are useful for quick experiments.

## Important Formulas

There is no numeric formula in this module. The useful mental model is:

\[
\text{element} = \text{opening tag} + \text{content} + \text{closing tag}
\]

Where:

- The opening tag starts an element, such as `<p>`.
- The content is what appears inside the element.
- The closing tag ends the element, such as `</p>`.

## Human-Readable Explanation

HTML tells the browser what the page contains. A heading is not just bigger text; it marks a section title. A link is not just blue underlined text; it creates navigation. This distinction matters because semantic tags help people, search engines, and assistive technologies understand the page.

JSFiddle provides a quick environment where HTML, CSS, and JavaScript can be tried without setting up a project. For early HTML practice, it helps isolate the structure of a page from the rest of a full application.

## Key Code Patterns

Create a heading, paragraph, and link:

```html
<h1>My First Page</h1>
<p>This paragraph explains the page.</p>
<a href="https://www.example.com">Visit example</a>
```

Add an image with alternative text:

```html
<img src="xray-example.png" alt="Example chest X-ray">
```

## Detailed Study Notes

HTML elements form a tree. The `html` element contains `head` and `body`. The `head` stores metadata such as page title and character encoding. The `body` stores visible content. Inside the body, headings, paragraphs, links, lists, and images describe the content users interact with.

A complete starter page:

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>My First HTML Page</title>
  </head>
  <body>
    <h1>My First HTML Page</h1>
    <p>This page uses headings, paragraphs, links, and images.</p>
  </body>
</html>
```

Lists should match the meaning of the content. Use an ordered list when sequence matters and an unordered list when it does not:

```html
<ol>
  <li>Open the lab.</li>
  <li>Edit the HTML.</li>
  <li>Run the preview.</li>
</ol>

<ul>
  <li>HTML</li>
  <li>CSS</li>
  <li>JavaScript</li>
</ul>
```

Links should describe their destination. "Read the HTML documentation" is clearer than "click here", especially for screen reader users who navigate link by link.

## Common Mistakes

- Leaving out `alt` text for meaningful images.
- Using heading levels out of order only for visual size.
- Forgetting that links need meaningful text.
- Writing unclosed or incorrectly nested tags.

## Takeaways

Module 1 builds the habit of using HTML tags for meaning. Clear structure makes later CSS and JavaScript easier to add.
