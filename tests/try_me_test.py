from hello.lib import try_me

def test_try_me():
    assert len(try_me('bonjour','salut')) > 0 