from nose.tools import *
from collaks import collaks
from collaks import collaks_naive


def test_conject():
    new = collaks.Conjecture(10000)
    new.conject()
