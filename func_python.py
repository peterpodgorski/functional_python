I = lambda a: a  # Identity/Idiot (Haskell: id)
M = lambda a: a(a)  # Mockingbird, aka self-application
K = lambda a: lambda b: a  # Kestrel (Haskell: const)
KI = lambda a: lambda b: b  # Kite (Haskell: const id)
# KI = lambda a: lambda b: K(I)(a)(b)  # Also Kite (KI-combinator)
# KI = lambda a: lambda b: C(K)(a)(b)  # Also Kite
C = lambda f: lambda a: lambda b: f(b)(a)  # Cardinal (Haskell: flip)
B = lambda f: lambda g: lambda a: f(g(a))  # Bluebird, aka composition (Haskell: .)

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
# OR = lambda p: lambda q: M(p)(q)  # also OR, but p(p) replaced by self-application

"""
In equality, the first one is used as the "selector", while the second
is both the first and second parameter, which is negated if it happens
to be selected as the second one.

   p  q     p q      q
BEQ(T)(T) -> T(T)(NOT(T)) -> p, being T,selects the first q, which happens to be T
BEQ(T)(F) -> T(F)(NOT(F)) -> p, being T, selects the first q, which happens to be F
BEQ(F)(T) -> F(T)(NOT(T)) -> F(T)(F) -> p, being F, selects the second q, which happens to be negated from T -> F
BEQ(F)(F) -> F(F)(NOT(F)) -> F(F)(T) -> p, being F, selects the second q, which happens to be negated from F -> T
"""
BEQ = lambda p: lambda q: p(q)(NOT(q))

once = lambda f: lambda a: f(a)
# once = lambda f: lambda a: I(f)(a)  # also once
twice = lambda f: lambda a: f(f(a))
thrice = lambda f: lambda a: f(f(f(a)))
zero = lambda f: lambda a: a
# zero = lambda f: lambda a: F(f)(a)  # also zero

succ = lambda n: lambda f: lambda a: f(n(f)(a))

"""
The below is also a successor!
Why it works? Because we're missing "a" here, which will get tugged along by B.
"""
# succ = lambda n: lambda f: B(f)(n(f))

pynum = lambda n: n(lambda x: x + 1)(0)

n0 = zero
n1 = once
n2 = twice
n3 = thrice
n4 = succ(n3)
n5 = succ(n4)

"""
Addition means adding 1 the number of times specified by n to k.
Adding 1 is just successor.
Numeral "k" itself is implemented as "do f a prescribed number of times to a".
    -> twice = lambda f: lambda a: f(f(a))
So "n + k" is "n successions on k"
"""
add = lambda n: lambda k: n(succ)(k)
