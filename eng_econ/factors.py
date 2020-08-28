from eng_econ import generate_dcostring


@generate_dcostring("F", "P", "Single payment compound amount")
def single_payment_compound_amount_factor(i, n):
    return (1 + i) ** n


@generate_dcostring("P", "F", "Single payment present worth")
def single_payment_present_worth_factor(i, n):
    return (1 + i) ** (-n)


@generate_dcostring("A", "F", "Uniform series sinking fund")
def uniform_series_sinking_fund_factor(i, n):
    return i / ((1 + i) ** n - 1)


@generate_dcostring("A", "P", "Capital recovery")
def capital_recovery_factor(i, n):
    temporary = (1 + i) ** n
    return i * temporary / (temporary - 1)


@generate_dcostring("F", "A", "Uniform series compound amount")
def uniform_series_compound_amount_factor(i, n):
    return ((1 + i) ** n - 1) / i
