def single_payment_compound_amount_factor(i, n):
    """
    Factor applies to F/P => to F (Future worth, value, or amount) given P (Present worth, value, or amount)

    :param i: Interest rate per interest period
    :param n: Number of compounding periods
    :return: Single payment compound amount factor
    """
    return (1 + i) ** n


def single_payment_present_worth_factor(i, n):
    """
    Factor applies to P/F => to P (Present worth, value, or amount) given F (Future worth, value, or amount)

    :param i: Interest rate per interest period
    :param n: Number of compounding periods
    :return: Single payment present worth factor
    """
    return (1 + i) ** (-n)


def uniform_series_sinking_fund_factor(i, n):
    """
    Factor applies to A/F => to A (Uniform amount per interest period) given F (Future worth, value, or amount)

    :param i: Interest rate per interest period
    :param n: Number of compounding periods
    :return: Uniform series sinking fund factor
    """
    return i / ((1 + i) ** n - 1)


def capital_recovery_factor(i, n):
    """
    Factor applies to A/P => to A (Uniform amount per interest period) given P (Present worth, value, or amount)

    :param i: Interest rate per interest period
    :param n: Number of compounding periods
    :return: Capital recovery factor
    """
    temporary = (1 + i) ** n
    return i * temporary / (temporary - 1)
