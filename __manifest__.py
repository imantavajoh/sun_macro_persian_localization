{
    "name": "Sun Macro Persian Localization",
    "version": "19.0.2.0.0",
    "category": "Localization",
    "summary": "Persian Localization Suite for Odoo 19",
    "description": """
Sun Macro Persian Localization
==============================

Features:
- Persian RTL Interface
- Persian UI Improvements
- Persian Font Support
- Persian Number Formatting
- Jalali utilities/settings
- Localization Settings
""",
    "author": "Sun Macro System",
    "depends": [
        "base",
        "web",
        "base_setup",
        "mail",
    ],
    "data": [
        "views/settings_views.xml",
        "views/menu_views.xml",
    ],
    "assets": {
        "web.assets_web": [
            "sun_macro_persian_localization/static/src/css/rtl.css",
            "sun_macro_persian_localization/static/src/js/localization.js",
            "sun_macro_persian_localization/static/src/js/persian_numbers.js",
            "sun_macro_persian_localization/static/src/js/persian_fields.js",
        ],
    },
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
