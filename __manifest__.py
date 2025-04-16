{
    "name": "My Custom Snippet",
    "version": "1.0",
    "category": "Website/Website",
    "summary": "Un snippet personalizado que muestra solo texto",
    "description": "Módulo que añade un snippet personalizado para mostrar un bloque de texto.",
    "author": "Tu Compañía",
    "website": "https://yourcompany.com",
    "license": "LGPL-3",
    "depends": ["website"],
    "data": [
        "views/snippets/s_text_block.xml",
        "views/snippets/snippets.xml"
    ],
    "assets": {
        "web.assets_frontend": [
            "my_custom_snippet/static/src/snippets/s_text_block/s_text_block.scss"
        ],
        "website.assets_editor": [
            "my_custom_snippet/static/src/snippets/s_text_block/s_text_block.js"
        ]
    },
    "installable": True,
    "application": False,
    "auto_install": False
}