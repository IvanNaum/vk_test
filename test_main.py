import pytest


# Integer tests
class TestInt:
    def test_one(self):
        assert 1 + 3 == 4

    def test_two(self):
        assert 5 * -7 == -35


class TestFloat:
    def test_one(self):
        assert -1.3 * 2.4 == -3.12

        def test_two(self):
            assert 3 / 5 == 0.6


class TestStr:
    @pytest.mark.parametrize('a,b,res', (
            ('', '', ''),
            ('abc', '', 'abc'),
            ('', 'abc', 'abc'),
            ('abc', 'abc', 'abcabc'),
            ('ab', 'cd', 'abcd'),
    ))
    def test_one(self, a, b, res):
        assert a + b == res

    # negative test
    def test_two(self):
        try:
            assert '3' + 2
        except TypeError:
            pass
