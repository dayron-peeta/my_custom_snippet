# snippet_o18

Custom module for Odoo 18 (that adds a personalized text). This is a simple snippet that follows the standard structure and conventions of Odoo 18 to can understand how it works.

## Module Structure

```
snippet_o18/
├── __init__.py
├── __manifest__.py
├── static/
│   └── src/
│       ├── img/
│       │   └── snippets_thumbs/
│       │       └── s_text_block.svg    <-- Snippet thumbnail (SVG)
│       └── snippets/
│           └── s_text_block/
│               ├── s_text_block.scss   <-- Custom styles (SCSS)
│               └── s_text_block.js     <-- Optional JS file (empty or with logic)
└── views/
    └── snippets/
        ├── s_text_block.xml            <-- QWeb template defining snippet HTML
        └── snippets.xml                <-- Snippet registration in the editor
```

## Snippet Definition

### Template (`s_text_block.xml`)

Defines the HTML structure of the snippet. For example:

```xml
<odoo>
  <template id="snippet_o18.s_text_block" name="Text Block">
    <section class="s_text_block pt40 pb40">
      <div class="container">
        <p>This is a custom text snippet. You can replace this content with your own.</p>
      </div>
    </section>
  </template>
</odoo>
```

### Snippet Registration (`snippets.xml`)

This file inherits the base snippet view from the `website` module and adds your snippet into the inner snippets container (with `id="snippet_content"`):

Make the snippet available in the inner section of the Website Editor.

```xml
<odoo>
<template id="snippet_o18.snippets" inherit_id="website.snippets" name="snippet_o18">
<xpath expr="//snippets[@id='snippet_content']" position="inside">
<t t-snippet="snippet_o18.s_text_block"
              t-thumbnail="/snippet_o18/static/src/img/snippets_thumbs/s_text_block.svg"
              string="Custom Text Block Inner"/>
</xpath>
</template>
</odoo>
```

Include the snippet in the category/group Text from the left panel and Index in the structure so that it appears in the search engine as a suggestion

```xml
<xpath expr="//snippets[@id='snippet_structure']" position="inside">
<t t-snippet="my_custom_snippet.s_text_block" string="Text" group="text">
<keywords>text, content, paragraph, article, body, description, information</keywords>
</t>
</xpath>
```

Duplicate the reference if you want the snippet to be visible or suggested from multiple categories.

```xml
<xpath expr="//snippets[@id='snippet_structure']" position="inside">
<t t-snippet="my_custom_snippet.s_text_block" string="Text" group="text">
<keywords>text, paragraph, article</keywords>
</t>
<t t-snippet="my_custom_snippet.s_text_block" string="Text" group="x">
<keywords>x, text, content, paragraph, article, body, description, information</keywords>
</t>
<t t-snippet="my_custom_snippet.s_text_block" string="Text" group="custom">
<keywords>custom, personalized</keywords>
</t>
</xpath>
```

Create an "X" category in the left panel if necessary

```xml
<xpath expr="//snippets[@id='snippet_groups']" position="inside">
<t snippet-group="x" t-snippet="website.s_snippet_group" string="X"
      t-thumbnail="/my_custom_snippet/static/src/img/snippets_thumbs/s_x_group.svg" />
</xpath>
```

## Assets (Styles and Logic)

### SCSS (`s_text_block.scss`)

Defines specific styles for the snippet:

```scss
.s_text_block {
  background-color: #f7f7f7;
  padding-top: 40px;
  padding-bottom: 40px;
  p {
    color: #333;
    font-size: 16px;
    line-height: 1.5;
  }
}
```

### JS (`s_text_block.js`)

Optional file to add dynamic behavior or interactivity:

```javascript
/** @odoo-module **/
// Optional JS for the s_text_block snippet.
```

## Thumbnail

The thumbnail image is located at:

```
snippet_o18/static/src/img/snippets_thumbs/s_text_block.svg
```

It is referenced in the registration with `t-thumbnail` to display it in the editor.

## Manifest

The `__manifest__.py` declares the website dependency, includes the view files, and registers the assets:

```python
{
    "name": "snippet_o18",
    "version": "1.0",
    "category": "Website/Website",
    "summary": "A custom snippet that shows a text block in Odoo 18",
    "description": "Module that adds a simple snippet to display text, following Odoo 18 best practices.",
    "author": "Your Company",
    "website": "https://yourcompany.com",
    "license": "LGPL-3",
    "depends": ["website"],
    "data": [
        "views/snippets/s_text_block.xml",
        "views/snippets/snippets.xml"
    ],
    "assets": {
        "web.assets_frontend": [
            "snippet_o18/static/src/snippets/s_text_block/s_text_block.scss"
        ],
        "website.assets_editor": [
            "snippet_o18/static/src/snippets/s_text_block/s_text_block.js"
        ]
    },
    "installable": True,
    "application": False,
    "auto_install": False
}
```
