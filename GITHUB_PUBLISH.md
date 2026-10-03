# GitHub Publishing Guide

## Recommended repository name

Use the exact technical module name so a direct clone creates a valid Odoo addon directory:

`sun_macro_persian_localization`

## Suggested repository description

Free Persian localization enhancements for Odoo 19: RTL, Persian fonts, Persian digits, and Jalali utilities.

## Suggested topics

`odoo` `odoo19` `persian` `farsi` `rtl` `jalali` `localization` `iran`

## First push

```bash
git init
git add .
git commit -m "Release Sun Macro Persian Localization 19.0.2.0.0"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/sun_macro_persian_localization.git
git push -u origin main
```

## Version tag

```bash
git tag -a v19.0.2.0.0 -m "Sun Macro Persian Localization 19.0.2.0.0"
git push origin v19.0.2.0.0
```

Then create a GitHub Release from tag `v19.0.2.0.0` and use `RELEASE_NOTES.md` as the release description.
