import pytest

I = lambda a: a  # Identity/Idiot (Haskell: id)
M = lambda a: a(a)  # Mockingbird
K = lambda a: lambda b: a  # Kestrel (Haskell: const)
KI = lambda a: lambda b: b  # Kite (Haskell: const id)
# KI = lambda a: lambda b: K(I)(a)(b)  # Also Kite (KI-combinator)
C = lambda f: lambda a: lambda b: f(b)(a)  # Cardinal (Haskell: flip)
# KI = lambda a: lambda b: C(K)(a)(b)  # Also Kite

# These are obtained by translating `lambda x, y: x if x else y` into
# pre-existing combinators
T = K  # True
F = KI  # False

NOT = lambda b: b(F)(T)  # where b is T or F
C_NOT = lambda b: C(b)

"""
AND(T)(T) -> T(T)(T) -> T
AND(F)(F) -> F(F)(F) -> F
but...
    p  q     p q  p     q
AND(T)(F) -> T(F)(T) -> F, because p is T, which selects 1st, which is q, which is F
    p  q     p q  p     q
AND(T)(F) -> F(T)(F) -> F, because p is F, which selects 2nd, which is p, which is F
"""
AND = lambda p: lambda q: p(q)(p)

"""
OR(T)(T) -> T(T)(T) -> T
OR(F)(F) -> F(F)(F) -> F
but...
   p  q     p p  q     q
OR(T)(F) -> T(T)(F) -> T, because p is T, which selects 1st
   p  q     p p  q     q
OR(T)(F) -> F(F)(T) -> T, because p is F, which selects 2nd
"""
OR = lambda p: lambda q: p(p)(q)


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


class Test_negation_selects_the_other_boolean:
    def test_of_T_is_F(self):
        assert NOT(T) == F

    def test_of_F_is_T(self):
        assert NOT(F) == T


class Test_Cardinal_impl_of_NOT:
    def test_C_NOT_of_T_of_1_2_behaves_like_F_of_1_2(self):
        assert C_NOT(T)(1)(2) == F(1)(2)


class Test_And:
    def test_of_T_T_is_T(self):
        assert AND(T)(T) == T

    def test_of_T_F_is_F(self):
        assert AND(T)(F) == F

    def test_of_F_T_is_F(self):
        assert AND(F)(T) == F

    def test_of_F_F_is_F(self):
        assert AND(F)(F) == F


class Test_Or:
    def test_of_T_T_is_T(self):
        assert OR(T)(T) == T

    def test_of_T_F_is_T(self):
        assert OR(T)(F) == T

    def test_of_F_T_is_T(self):
        assert OR(F)(T) == T

    def test_of_F_F_is_F(self):
        assert OR(F)(F) == F
