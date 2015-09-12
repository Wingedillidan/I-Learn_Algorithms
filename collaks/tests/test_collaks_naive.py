from nose.tools import *
from collaks import collaks
from collaks import collaks_naive


def test_conject():
    naive = collaks_naive.Conjecture(10000)
    naive.conject()
