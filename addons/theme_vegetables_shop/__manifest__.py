# -*- coding: utf-8 -*-
{
    'name': "theme_vegetables_shop",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Theme/Environment',
    'version': '0.1',
    'depends': ['theme_common'],
    'data': [
        # THEME
        'views/assets.xml',
        'views/template.xml',
        'views/s_product_list.xml',
        # SNIPPETS
        'views/snippets/s_panel_extended.xml',
        'views/snippets/s_share_extended.xml',
        'views/snippets/s_well_extended.xml',
    ],
    'images': [
        'static/description/vegetables_screenshot.jpg',
    ]
}
