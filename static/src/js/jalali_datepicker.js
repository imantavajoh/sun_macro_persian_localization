/** @odoo-module **/

import { rpc } from "@web/core/network/rpc";


async function checkJalaliStatus() {

    const result = await rpc(
        "/sun_macro_persian_localization/jalali/status"
    );

    if (result.enabled) {

        console.log(
            "Sun Macro Jalali Calendar Enabled"
        );

    } else {

        console.log(
            "Sun Macro Jalali Calendar Disabled"
        );

    }

}


checkJalaliStatus();