WIN-BRC Why 'n' How: Automated testing in software tools
--------------------------------------------------------


[![pauldmccarthy](https://circleci.com/gh/pauldmccarthy/win-brc-automated-testing.svg?style=svg)](https://circleci.com/gh/pauldmccarthy/win-brc-automated-testing)


This repository contains some example code used to demonstrate automated
testing of a Python project using `pytest`, `coverage`, and Github-CircleCI
integration.


The `analysis/main.py` file contains a simple Python program which performs
linear regression using Ordinary Least Squares. Some unit tests for this
program are available in `tests/test_main.py`, and a CircleCI configuration
for running the tests is in `.circleci/config.yml`.


This example accompanies a talk given at the Department of Psychiatry,
Unversity of Oxford, on Thursday February 13th, 2020. This talk is part of a
series of talks run jointly by the Wellcome Trust Centre for Integrative
Neuroimaging and the Oxford Health Biomedical Research Centre.


The slides for the talk are available in the `presentation/` directory.
