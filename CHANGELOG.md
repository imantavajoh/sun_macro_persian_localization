# Changelog

## [19.0.2.0.0] - 2026-10-03

### Added
- Dedicated Persian localization settings in Odoo Settings.
- Optional RTL web-client mode.
- Vazirmatn and Shabnam font selection.
- Optional Persian digits for common float, integer, and monetary fields.
- Jalali/Gregorian Python conversion utilities using `jdatetime`.

### Release cleanup
- Declared `jdatetime` as an external Python dependency.
- Switched web-client assets to the Odoo 19 `web.assets_backend` bundle.
- Removed development `console.log` diagnostics.
- Removed no-op Jalali frontend debug patches.
- Removed unused `mail` dependency and unused XML files.
- Removed IRANSans from the public distribution.
- Added open-source documentation and font licensing notices.
