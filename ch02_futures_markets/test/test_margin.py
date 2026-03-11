from src.margin_account import MarginAccount


def test_margin_call():
    account = MarginAccount(initial_margin=10000, maintenance_margin=7000)

    call = account.mark_to_market(-4000)

    assert call == 4000
    assert account.balance == 10000
