import hello


def test_hello1():
    res = hello("Bob")
    assert "hello Bob" == res

