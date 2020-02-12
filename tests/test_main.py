#!/usr/bin/env python

import numpy as np

import analysis.main as main

test_model = np.array([[0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
                       [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]]).T
test_data  = (test_model[:, 0] * 5) + (test_model[:, 1] * 20)


def test_ols():
    fit, err = main.ols(test_data, test_model)
    assert np.isclose(fit, [5, 20]).all()
    assert np.isclose(err, 0)      .all()


def test_main():
    np.savetxt('data.txt', test_data)
    np.savetxt('model.txt', test_model)

    main.main('data.txt', 'model.txt', 'pes.txt', 'residuals.txt')

    fit = np.loadtxt('pes.txt')
    err = np.loadtxt('residuals.txt')

    assert np.isclose(fit, [5, 20]).all()
    assert np.isclose(err, 0)      .all()
