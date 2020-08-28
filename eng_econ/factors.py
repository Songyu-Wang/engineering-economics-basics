def single_payment_compound_amount(i, n):
    """
    to F(Future worth, value, or amount) given P(Present worth, value, or amount)
    (F/P, i%, n)\n
    :param i: Interest rate per interest period\n
    :param n: Number of compounding periods\n
    :return: Single payment compound amount factor
    """
    return (1 + i) ** n
