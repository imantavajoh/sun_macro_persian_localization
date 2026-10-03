from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"


    enable_rtl = fields.Boolean(
        string="فعال‌سازی رابط راست‌چین",
        config_parameter="sun_macro_persian_localization.enable_rtl",
        default=True,
    )


    use_persian_numbers = fields.Boolean(
        string="نمایش اعداد فارسی",
        config_parameter="sun_macro_persian_localization.use_persian_numbers",
        default=True,
    )


    use_persian_separator = fields.Boolean(
        string="جداکننده هزارگان فارسی",
        config_parameter="sun_macro_persian_localization.use_persian_separator",
        default=True,
    )


    iran_currency_display = fields.Selection(
        [
            ("irr", "ریال ایران"),
            ("irt", "تومان"),
        ],
        string="واحد نمایش پول ایران",
        default="irr",
        config_parameter="sun_macro_persian_localization.iran_currency_display",
    )


    jalali_date = fields.Boolean(
        string="فعال‌سازی تاریخ شمسی",
        config_parameter="sun_macro_persian_localization.jalali_date",
        default=False,
    )


    font_family = fields.Selection(
        [
            ("vazirmatn", "Vazirmatn"),
            ("shabnam", "Shabnam"),
        ],
        string="فونت فارسی",
        default="vazirmatn",
        config_parameter="sun_macro_persian_localization.font_family",
    )