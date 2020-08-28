import pytest

import eng_econ.factors as f

test_input = "i,n,expected"


@pytest.mark.parametrize(
    test_input, [(0.005, 1, 1.0050), (0.01, 10, 1.1046), (0.08, 5, 1.4693)]
)
def test_single_payment_compound_amount_factor(i, n, expected):
    assert round(f.single_payment_compound_amount_factor(i, n), 4) == expected


@pytest.mark.parametrize(
    test_input, [(0.005, 1, 0.9950), (0.01, 10, 0.9053), (0.08, 5, 0.6806)]
)
def test_single_payment_present_worth_factor(i, n, expected):
    assert round(f.single_payment_present_worth_factor(i, n), 4) == expected


@pytest.mark.parametrize(
    test_input, [(0.005, 1, 1.0000), (0.01, 10, 0.0956), (0.08, 5, 0.1705)]
)
def test_uniform_series_sinking_fund_factor(i, n, expected):
    assert round(f.uniform_series_sinking_fund_factor(i, n), 4) == expected


@pytest.mark.parametrize(
    test_input, [(0.005, 1, 1.0050), (0.01, 10, 0.1056), (0.08, 5, 0.2505)]
)
def test_capital_recovery_factor(i, n, expected):
    assert round(f.capital_recovery_factor(i, n), 4) == expected


@pytest.mark.parametrize(
    test_input, [(0.005, 1, 1.0000), (0.01, 10, 10.4622), (0.08, 5, 5.8666)]
)
def test_uniform_series_compound_amount_factor(i, n, expected):
    assert round(f.uniform_series_compound_amount_factor(i, n), 4) == expected


@pytest.mark.parametrize(
    test_input, [(0.005, 1, 0.9950), (0.01, 10, 9.4713), (0.08, 5, 3.9927)]
)
def test_uniform_series_present_worth_factor(i, n, expected):
    assert round(f.uniform_series_present_wortht_factor(i, n), 4) == expected


@pytest.mark.parametrize(
    test_input, [(0.005, 1, 0.0000), (0.01, 10, 41.8435), (0.08, 5, 7.3724)]
)
def test_uniform_gradient_present_worth_factor(i, n, expected):
    assert round(f.uniform_gradient_present_worth_factor(i, n), 4) == expected


@pytest.mark.parametrize(
    test_input, [(0.005, 1, 0.0000), (0.01, 10, 46.2213), (0.08, 5, 10.8325)]
)
def test_uniform_gradient_future_worth_factor(i, n, expected):
    assert round(f.uniform_gradient_future_worth_factor(i, n), 4) == expected


@pytest.mark.parametrize(
    test_input, [(0.005, 1, 0.0000), (0.01, 10, 4.4179), (0.08, 5, 1.8465)]
)
def test_uniform_gradient_uniform_series_factor(i, n, expected):
    assert round(f.uniform_gradient_uniform_series_factor(i, n), 4) == expected
