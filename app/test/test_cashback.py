from app.test.cashback import cashback


def test_cashback_under_limit():
    result = cashback(1000)

    assert 50 == result

def test_cashback_over_limit():
    result = cashback(1_000_000)

    assert 3_000==result
