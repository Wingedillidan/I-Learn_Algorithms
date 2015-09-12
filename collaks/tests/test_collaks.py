from nose.tools import *
from collaks import collaks
from collaks import collaks_naive


def test_conject():
    naive = collaks_naive.Conjecture(100)
    naive.conject()
    new = collaks.Conjecture(100)
    new.conject()
    assert_equal(naive.maths, new.maths)
