import jdatetime


def gregorian_to_jalali(date_value):
    """
    Convert Gregorian date to Jalali date
    """

    if not date_value:
        return False

    result = jdatetime.date.fromgregorian(
        date=date_value
    )

    return result.strftime("%Y/%m/%d")


def jalali_to_gregorian(date_value):
    """
    Convert Jalali date to Gregorian date
    """

    if not date_value:
        return False

    year, month, day = map(
        int,
        date_value.split("/")
    )

    result = jdatetime.date(
        year,
        month,
        day
    )

    return result.togregorian()