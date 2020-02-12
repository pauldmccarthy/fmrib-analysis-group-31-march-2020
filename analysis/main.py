#!/usr/bin/env python
import numpy as np
import sys

def ols(data, model):
    """Perform ordinary-least-squares regression. """
    fit   = np.linalg.inv(model.T @ model) @ model.T @ data
    error = data - (model @ fit)
    return fit, error

def main(datafile, designfile, fitfile, errfile):
    """Fit a linear model to some data. """

    # load data and model
    data  = np.loadtxt(datafile)
    model = np.loadtxt(designfile)

    # perform OLS regression
    fit, error = ols(data, model)

    # save parameter estimates and residuals
    np.savetxt(fitfile, fit)
    np.savetxt(errfile, error)

if __name__ == '__main__':
    datafile   = sys.argv[1]
    designfile = sys.argv[2]
    fitfile    = sys.argv[3]
    errfile    = sys.argv[4]
    main(datafile, designfile, fitfile, errfile)
