import pytest

I = lambda a: a  # Identity/Idiot (Haskell: id)
M = lambda a: a(a)  # Mockingbird
K = lambda a: lambda b: a  # Kestrel (Haskell: const)
KI = lambda x: lambda y: y  # Kite (Haskell: const id)
# KI = lambda x: lambda y: K(I)(x)(y)  # Also Kite (KI-combinator)
C = lambda f: lambda a: lambda b: f(b)(a)


def test_identity_or_1_is_1():
    assert I(1) == 1


class Test_Mockingbird_repeats_the_argument:
    def test_of_I_is_I(self):
        assert M(I) == I

    def test_of_Mockingbird_explodes_because_Python(self):
        with pytest.raises(RuntimeError):
            assert M(M)


class Test_Kestrel_gives_back_first_argument:
    def test_of_Identity_and_Mockingbird_is_Identity(self):
        assert K(I)(M) == I

    def test_of_K_and_M_is_K(self):
        assert K(K)(M) == K


class Test_Kite_gives_back_second_argument:
    def test_of_I_and_M_is_M(self):
        assert KI(I)(M) == M


class Test_Cardinal_flips_arguments_around:
    def test_of_K_I_M_calls_K_of_M_I_which_is_M(self):
        assert C(K)(I)(M) == M
