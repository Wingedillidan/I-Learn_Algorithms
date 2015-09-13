from nose.tools import *
from collaks import collaks
from collaks import collaks_naive


def test_conject():
    new = collaks.Conjecture(10000)
    new.proc()
    naive = collaks_naive.Conjecture(10000)
    naive.conject()

    assert_equal(new.maths, naive.maths)
