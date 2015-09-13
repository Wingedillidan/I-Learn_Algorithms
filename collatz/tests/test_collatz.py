from nose.tools import *
from collatz import collatz
from collatz import collatz_naive


def test_conject():
    new = collatz.Conjecture(10000)
    new.proc()
    naive = collatz_naive.Conjecture(10000)
    naive.conject()

    assert_equal(new.maths, naive.maths)
