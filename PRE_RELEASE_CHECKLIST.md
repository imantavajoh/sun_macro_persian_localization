# Pre-release checklist — 19.0.2.0.0

## Completed during repository cleanup

- [x] Manifest parses successfully.
- [x] Version is `19.0.2.0.0`.
- [x] License is declared as `LGPL-3`.
- [x] `jdatetime` is declared under `external_dependencies`.
- [x] XML files parse successfully.
- [x] Python source passes syntax compilation.
- [x] JavaScript files pass syntax checking.
- [x] Numeric Python helpers passed basic conversion tests.
- [x] Development `console.log` diagnostics removed.
- [x] Python cache files removed from release package.
- [x] IRANSans removed from the public package.
- [x] Legacy `sms_fa_localization` references removed.
- [x] No local Odoo/database path was found in the release source.
- [x] Bundled font licensing notice added.

## Final tests to run on the maintainer's Odoo 19 environment

- [ ] Install `jdatetime` in the same Python environment used by Odoo.
- [ ] Fresh-install the module on a test database.
- [ ] Upgrade an existing `19.0.2.0.0` development installation.
- [ ] Confirm Settings opens without an XML/view error.
- [ ] Confirm RTL toggle on/off after browser refresh.
- [ ] Confirm Vazirmatn and Shabnam selection after browser refresh.
- [ ] Confirm Persian-number toggle for integer, float, and monetary fields.
- [ ] Check the browser console for module-related errors.
- [ ] Check the Odoo server log for module-related tracebacks.

A live Odoo install/upgrade test is intentionally left to the maintainer environment because this repository-cleanup environment does not contain an Odoo 19 server or `jdatetime` runtime.
