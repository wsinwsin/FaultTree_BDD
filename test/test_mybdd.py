import pytest
from ft_bdd import mybdd as mb

def test_mybdd1():
    bdd = mb.BDD()
    a = bdd.var('a')
    b = bdd.var('b')
    c = bdd.And(a,b)
    c.todot()
    assert type(c) == mb.Variable

def test_mybdd2():
    bdd = mb.BDD()
    a = bdd.var('a')
    b = bdd.var('b')
    c = bdd.Or(a,b)
    c.todot()
    assert type(c) == mb.Variable

def test_mybdd3():
    bdd = mb.BDD()
    a = bdd.var('a')
    b = bdd.var('b')
    c = bdd.var('c')
    d = bdd.Not(c)
    e = mb.createOrGate(bdd,[a,b,d])
    e.todot()
    assert type(c) == mb.Variable

def test_mybdd4():
    bdd = mb.BDD()
    a = bdd.var('a')
    b = bdd.var('b')
    c = bdd.var('c')
    d = bdd.Not(c)
    e = mb.createAndGate(bdd,[a,b,d])
    e.todot()
    assert type(c) == mb.Variable

def test_mybdd5():
    bdd = mb.BDD()
    a = bdd.var('a')
    b = bdd.var('b')
    c = bdd.var('c')
    d = bdd.var('d')
    e = bdd.var('e')
    f = bdd.var('f')
    g = bdd.var('g')
    g1 = bdd.And(a,b)
    g2 = bdd.And(c,d)
    g3 = bdd.Not(e)
    g4 = bdd.And(g3,f)
    g5 = bdd.Not(g2)
    te = mb.createOrGate(bdd,[g1,g4,g5])
    te.todot()
    assert type(te) == mb.Variable

def test_mybdd6():
    bdd = mb.BDD()
    a = bdd.var('a')
    print(a.low)
    repr(a.low)
    print(a)
    repr(a)
    assert True

def test_mybdd7():
    bdd = mb.BDD()
    a = bdd.var('a')
    b = bdd.var('b')
    c = bdd.var('c')
    d = bdd.var('d')
    e = bdd.var('e')
    f = bdd.var('f')
    g = bdd.var('g')
    g1 = bdd.Or(a,b)
    g2 = bdd.Or(c,d)
    g3 = bdd.Not(e)
    g4 = bdd.Or(g3,f)
    g5 = bdd.Not(g2)
    te = mb.createAndGate(bdd,[g1,g4,g5])
    te.todot()
    assert type(te) == mb.Variable

def test_mybdd8():
    bdd = mb.BDD()
    a = bdd.var('a')
    b = bdd.var('b')
    c = bdd.var('c')
    g1 = bdd.Or(a,b)
    g2 = bdd.And(a,c)
    te = mb.createOrGate(bdd,[a,g1,g2])
    te.todot()
    assert type(te) == mb.Variable

def test_mybdd9():
    bdd = mb.BDD()
    a = bdd.var('a')
    a = bdd.var('a')
    b = bdd.var('b')
    c = bdd.var('c')
    d = bdd.var('d')
    bdd.And(a,a)
    g1 = bdd.And(a,b)
    g2 = bdd.And(c,d)
    te = bdd.And(g1,g2)
    assert True

def test_mybdd10():
    bdd = mb.BDD()
    a = bdd.var('a')
    b = bdd.var('b')
    g1 = bdd.And(b,a)
    g2 = bdd.Or(b,a)
    assert True
    