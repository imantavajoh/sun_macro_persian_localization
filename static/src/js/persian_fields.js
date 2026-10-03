/** @odoo-module **/

import { registry } from "@web/core/registry";
import { patch } from "@web/core/utils/patch";
import { toPersianDigits } from "./persian_numbers";

const fields = registry.category("fields");
const patched = new Set();

function patchNumericField(name) {
    if (!fields.contains(name)) {
        return;
    }
    const definition = fields.get(name);
    const Component = definition && definition.component;
    if (!Component || patched.has(Component)) {
        return;
    }
    patched.add(Component);

    patch(Component.prototype, {
        get formattedValue() {
            return toPersianDigits(super.formattedValue);
        },
    });
}

for (const fieldName of ["float", "integer", "monetary"]) {
    patchNumericField(fieldName);
}
