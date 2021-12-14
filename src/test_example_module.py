# to make this work, need to declare /src as part of a package by placing
# the file '__init__.py' in the subdirectory /src
import src.example_module as em


def test_square_it():
    assert em.square_it(4) == 16


def test_decrement_it():
    assert em.decrement_it(11) == 10
