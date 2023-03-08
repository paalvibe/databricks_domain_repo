# Nyc Taxi data - experimental project

Do some experiments with the NYC taxi data

# How to run tests

## Install pipenv

``````bash
pipenv install --dev
``````

## Run tests from project folder:

``````bash
nyctaxi$ pytest tests/
=================================================================================== test session starts ====================================================================================
platform darwin -- Python 3.10.9, pytest-7.2.2, pluggy-1.0.0
rootdir: /Users/paalvibe/dev/work/databricks/databricks_domain_repo/projects/nyctaxi
collected 14 items

tests/libs/age/test_gen_age.py .                                                                                                                                                     [  7%]
tests/libs/chain/test_chain.py .                                                                                                                                                     [ 14%]
tests/libs/dataframe/test_dfdiff.py ...........                                                                                                                                      [ 92%]
tests/libs/periods/test_group_by_day.py .                                                                                                                                            [100%]

===================================================================================== warnings summary =====================================================================================
tests/libs/dataframe/test_dfdiff.py: 14 warnings
  /Users/paalvibe/.local/share/virtualenvs/databricks_domain_repo-QLSTlpx-/lib/python3.10/site-packages/pyspark/sql/pandas/utils.py:37: DeprecationWarning: distutils Version classes are deprecated. Use packaging.version instead.
    if LooseVersion(pandas.__version__) < LooseVersion(minimum_pandas_version):

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================================================================== 14 passed, 14 warnings in 88.60s (0:01:28) ========================================================================
``````