/** @odoo-module **/

const PERSIAN_DIGITS = "۰۱۲۳۴۵۶۷۸۹";

export function toPersianDigits(value) {
    if (value === null || value === undefined) {
        return value;
    }
    return String(value).replace(/[0-9]/g, (digit) => PERSIAN_DIGITS[digit]);
}

export function formatPersianNumber(value) {
    if (value === null || value === undefined || value === "") {
        return value;
    }
    const parts = String(value).split(".");
    parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, "٬");
    return toPersianDigits(parts.join("."));
}
