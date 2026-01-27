from ch01_market_structure.src.contracts import ForwardContract, EuropeanCall, EuropeanPut, payoff


def test_forward_payoff():
    fwd = ForwardContract(K=100)
    assert payoff(fwd, ST=110, position="long") == 10
    assert payoff(fwd, ST=90, position="long") == -10
    assert payoff(fwd, ST=110, position="short") == -10


def test_call_payoff():
    call = EuropeanCall(K=100)
    assert payoff(call, ST=110) == 10
    assert payoff(call, ST=90) == 0


def test_put_payoff():
    put = EuropeanPut(K=100)
    assert payoff(put, ST=90) == 10
    assert payoff(put, ST=110) == 0
