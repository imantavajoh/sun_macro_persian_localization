from odoo import http
from odoo.http import request


class SunMacroLocalizationController(http.Controller):

    @http.route(
        "/sun_macro_persian_localization/font",
        type="jsonrpc",
        auth="user",
    )
    def get_font(self):
        font = request.env["ir.config_parameter"].sudo().get_param(
            "sun_macro_persian_localization.font_family",
            "vazirmatn",
        )
        if font not in {"vazirmatn", "shabnam"}:
            font = "vazirmatn"
        return {"font": font}

    @http.route(
        "/sun_macro_persian_localization/jalali/status",
        type="jsonrpc",
        auth="user",
    )
    def get_jalali_status(self):
        value = request.env["ir.config_parameter"].sudo().get_param(
            "sun_macro_persian_localization.jalali_date",
            "False",
        )
        return {"enabled": value == "True"}
