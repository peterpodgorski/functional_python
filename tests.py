import pytest

from func_python import *


def test_identity_or_1_is_1():
    assert I(1) == 1


class Test_Mockingbird_repeats_the_argument:
    def test_of_I_is_I(self):
        assert M(I) == I

    def test_of_Mockingbird_explodes_because_Python(self):
        with pytest.raises(RuntimeError):
            assert M(M)


class Test_Mockingbird_once_removed_acting_as_OR:
    def test_of_T_T_is_T(self):
        assert M(T)(T) == T

    def test_of_T_F_is_T(self):
        assert M(T)(F) == T

    def test_of_F_T_is_T(self):
        assert M(F)(T) == T

    def test_of_F_F_is_F(self):
        assert M(F)(F) == F


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


class Test_equality:
    def test_of_T_T_is_T(self):
        assert BEQ(T)(T) == T

    def test_of_T_F_is_F(self):
        assert BEQ(T)(F) == F

    def test_of_F_T_is_F(self):
        assert BEQ(F)(T) == F

    def test_of_F_F_is_T(self):
        assert BEQ(F)(F) == T


class Test_Church_encodings_for_numerals:
    def test_NOT_applied_once_to_T_gives_F(self):
        assert once(NOT)(T) == F

    def test_NOT_applied_twice_to_T_gives_T(self):
        assert twice(NOT)(T) == T

    def test_NOT_applied_thrice_to_T_gives_F(self):
        assert thrice(NOT)(T) == F

    def test_NOT_applied_zero_times_to_T_gives_T(self):
        assert zero(NOT)(T) == T

    def test_successor_of_once_works_like_twice(self):
        assert succ(once)(NOT)(T) == twice(NOT)(T)

    def test_successor_of_zero_translates_to_python_1(self):
        assert pynum(succ(zero)) == 1

    def test_successor_of_successor_of_zero_is_2(self):
        assert pynum(succ(succ(zero))) == 2


class Test_function_composition_slash_pipeline:
    def test_of_not_not_T_is_T(self):
        assert B(NOT)(NOT)(T) == T

    def test_of_succ_succ_n1_is_3_same_as_succ_of_succ_of_n1(self):
        assert pynum(B(succ)(succ)(n1)) == pynum(succ(succ(n1))) == pynum(n3)


class Test_addition:
    def test_add_3_and_4_gives_7(self):
        assert pynum(add(n3)(n4)) == 7


class Test_multiplication:
    def test_mul_3_and_4_gives_12(self):
        assert pynum(mul(n3)(n4)) == 12


class Test_exponentiation:  # noqa
    def test_exp_2_and_3_is_9(self):
        assert pynum(exp(n2)(n3)) == 8


class Test_is_zero:  # noqa
    def test_of_0_is_true(self):
        assert iszero(n0) == T

    def test_of_1_is_false(self):
        assert iszero(n1) == F

    def test_of_2_is_false(self):
        assert iszero(n2) == F

    def test_of_3_is_false(self):
        assert iszero(n3) == F


class Test_vireo_closure:
    def test_of_I_and_M_returns_I_when_given_K(self):
        vim = V(I)(M)
        assert vim(K) == I

    def test_of_I_and_M_returns_I_when_given_KI(self):
        vim = V(I)(M)
        assert vim(KI) == M

    def test_of_n1_and_n3_returns_n1_when_given_K(self):
        v = V(n1)(n3)
        assert v(K) == n1
