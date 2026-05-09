# HTML, CSS, and JavaScript - Module 2

<span class="track-badge fullstack">IBM Full Stack Software Developer</span>

## What This Covers

Module 2 covers common HTML5 tags and additional form elements, including `fieldset` and `legend`. It emphasizes semantic layout and clear grouping of related controls.

## Core Ideas

- HTML5 semantic tags describe page regions.
- `header`, `nav`, `main`, `section`, `article`, and `footer` improve document readability.
- Forms should use labels so users know what each input means.
- `fieldset` groups related form controls.
- `legend` gives a visible and semantic title to a field group.

## Important Formulas

There is no mathematical formula in this module. The structural pattern is:

\[
\text{form section} = \text{fieldset} + \text{legend} + \text{related controls}
\]

Where:

- `fieldset` creates the group.
- `legend` names the group.
- Related controls are inputs, checkboxes, radio buttons, or selects that belong together.

## Human-Readable Explanation

Semantic HTML makes a page easier to scan and maintain. A navigation menu should live in `nav`; the main unique content should live in `main`; a standalone content piece can use `article`; and supporting page information can live in `footer`.

For forms, grouping matters. If a form asks for contact preferences, shipping details, or account settings, related inputs should be grouped together. `fieldset` and `legend` make that grouping visible to users and meaningful to assistive technologies.

## Key Code Patterns

Semantic page layout:

```html
<header>
  <h1>Course Notes</h1>
</header>
<nav>
  <a href="/">Home</a>
</nav>
<main>
  <section>
    <h2>Module Summary</h2>
    <p>Semantic HTML improves structure.</p>
  </section>
</main>
<footer>
  <p>End of page.</p>
</footer>
```

Group related form controls:

```html
<fieldset>
  <legend>Contact preference</legend>

  <label>
    <input type="radio" name="contact" value="email">
    Email
  </label>

  <label>
    <input type="radio" name="contact" value="phone">
    Phone
  </label>
</fieldset>
```

## Detailed Study Notes

Semantic layout tags do not automatically style a page in a dramatic way. Their main value is meaning. A `main` element tells browsers and assistive technologies where the unique content starts. A `nav` element identifies navigation. An `article` can stand alone, while a `section` groups related content inside a larger page.

Use this pattern for page-level structure:

```html
<body>
  <header>
    <h1>Course Catalog</h1>
  </header>

  <nav aria-label="Primary">
    <a href="/">Home</a>
    <a href="/courses">Courses</a>
  </nav>

  <main>
    <article>
      <h2>HTML Basics</h2>
      <p>HTML gives the page structure.</p>
    </article>
  </main>
</body>
```

Use `fieldset` when controls share one question or category:

```html
<fieldset>
  <legend>Choose your course interests</legend>

  <label>
    <input type="checkbox" name="interest" value="ai">
    AI
  </label>

  <label>
    <input type="checkbox" name="interest" value="web">
    Web development
  </label>
</fieldset>
```

Radio buttons with the same `name` create one mutually exclusive group. Checkboxes with the same `name` allow multiple selections. A `select` is useful when there are many choices and showing all options would take too much space.

## Common Mistakes

- Using `section` without a heading.
- Replacing every semantic element with `div`.
- Creating form inputs without labels.
- Using `legend` outside of `fieldset`.
- Grouping unrelated controls together.

## Takeaways

Module 2 strengthens HTML structure. Semantic regions and grouped forms make pages clearer for users, developers, and assistive technology.
