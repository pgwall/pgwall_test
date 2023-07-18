Integration testing
=======================

To support `integration testing <https://en.wikipedia.org/wiki/Integration_testing>`__ the unit tests in **pgwall_test**
include a parallel set of tests reside in the existing test framework and
can be activated if ``PGWALL_TEST_INTEGRATION_TEST`` environment
variable is set to any value:

Example variable:

.. code-block::

    export PGWALL_TEST_INTEGRATION_TEST="true"
    make test
