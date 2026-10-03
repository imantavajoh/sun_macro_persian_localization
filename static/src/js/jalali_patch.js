/** @odoo-module **/

import { DateTimeField } from "@web/views/fields/datetime/datetime_field";


console.log(
    "Sun Macro Jalali Patch Loaded",
    DateTimeField
);
import { patch } from "@web/core/utils/patch";


patch(
    DateTimeField.prototype,
    {
        setup() {

            super.setup(...arguments);

            console.log(
                "Sun Macro Date Field Active",
                this
            );

        },
    }
);