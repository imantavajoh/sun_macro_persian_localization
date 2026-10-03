# Sun Macro Persian Localization for Odoo 19

Free and open-source Persian localization enhancements for **Odoo 19**, developed by **Sun Macro System**.

**Technical module name:** `sun_macro_persian_localization`  
**Release:** `19.0.2.0.0`  
**License:** LGPL-3.0

[راهنمای فارسی](README.fa.md)

## Features

- Optional RTL layout for the Odoo backend web client
- Global Persian font selection
  - Vazirmatn
  - Shabnam
- Optional Persian digits for common `float`, `integer`, and `monetary` fields
- Jalali/Gregorian conversion helpers based on `jdatetime`
- Dedicated localization section in Odoo Settings

### Jalali status in this release

Version `19.0.2.0.0` includes the Jalali configuration flag and Python conversion utilities. A complete replacement of Odoo's frontend Date/DateTime picker is **not** claimed as a finished feature in this release.

## Requirements

- Odoo 19.0
- Python environment supported by your Odoo 19 installation
- `jdatetime`

Install the Python dependency:

```bash
pip install jdatetime
```

The dependency is also declared in `__manifest__.py` under `external_dependencies`.

## Installation

Clone the repository directly into a directory listed in your Odoo `addons_path`:

```bash
git clone https://github.com/YOUR_USERNAME/sun_macro_persian_localization.git
```

Then:

1. Restart Odoo.
2. Update the Apps List.
3. Search for **Sun Macro Persian Localization**.
4. Install the module.
5. Open Odoo **Settings** and configure the localization options.
6. Refresh the browser after changing frontend localization settings.

## Upgrade

```bash
python odoo-bin -c odoo.conf -d YOUR_DATABASE -u sun_macro_persian_localization
```

Adjust the command for your Odoo installation.

## Scope

This release targets the authenticated **Odoo backend web client**. Website, Portal, POS, and PDF/QWeb report localization are not included unless explicitly stated in a future release.

## Font licenses

The bundled Vazirmatn and Shabnam fonts are distributed under the **SIL Open Font License 1.1**. See [`FONT_LICENSES.md`](FONT_LICENSES.md) and [`static/src/fonts/OFL-1.1.txt`](static/src/fonts/OFL-1.1.txt).

IRANSans is **not included** in this open-source repository.

## Contributing

Bug reports and pull requests are welcome. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

The module source code is licensed under **GNU LGPL v3**. Bundled fonts remain under their respective OFL-1.1 licenses.

## Author

**Sun Macro System**
