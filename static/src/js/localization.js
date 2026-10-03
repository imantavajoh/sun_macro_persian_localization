/** @odoo-module **/

import { rpc } from "@web/core/network/rpc";

async function applySunMacroFont() {
    try {
        const result = await rpc("/sun_macro_persian_localization/font");
        const allowedFonts = new Set(["vazirmatn", "shabnam"]);
        const font = allowedFonts.has(result?.font) ? result.font : "vazirmatn";

        const apply = () => {
            if (!document.body) {
                return;
            }
            document.body.classList.remove("font-vazirmatn", "font-shabnam");
            document.body.classList.add(`font-${font}`);
        };

        if (document.readyState === "loading") {
            document.addEventListener("DOMContentLoaded", apply, { once: true });
        } else {
            apply();
        }
    } catch {
        // Do not block Odoo web client if localization settings are unavailable.
    }
}

applySunMacroFont();
