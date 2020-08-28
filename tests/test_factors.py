import pytest

import eng_econ.factors as f


@pytest.mark.parametrize(
    "i,n,expected", [(0.005, 1, 1.0050), (0.01, 10, 1.1046), (0.08, 5, 1.4693)]
)
def test_single_payment_compound_amount(i, n, expected):
    assert round(f.single_payment_compound_amount(i, n), 4) == expected
