# -*- coding: utf-8 -*-

PERSIAN_DIGITS = "۰۱۲۳۴۵۶۷۸۹"
ENGLISH_DIGITS = "0123456789"


def to_persian_digits(value):
    """
    تبدیل اعداد انگلیسی به فارسی
    """

    if value is None:
        return ""

    return str(value).translate(
        str.maketrans(
            ENGLISH_DIGITS,
            PERSIAN_DIGITS
        )
    )


def to_english_digits(value):
    """
    تبدیل اعداد فارسی به انگلیسی
    """

    if value is None:
        return ""

    return str(value).translate(
        str.maketrans(
            PERSIAN_DIGITS,
            ENGLISH_DIGITS
        )
    )


def format_number(value):
    """
    نمایش عدد با جداکننده هزارگان فارسی
    """

    if value is None:
        return ""

    value = float(value)

    result = "{:,.0f}".format(value)

    result = result.replace(",", "٬")

    return to_persian_digits(result)