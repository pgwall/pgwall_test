#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Integration Tests for `pgwall_test` package."""

import os

import unittest
from pgwall_test import pgwall_testcmd

SKIP_REASON = 'PGWALL_TEST_INTEGRATION_TEST ' \
              'environment variable not set, cannot run integration ' \
              'tests'

@unittest.skipUnless(os.getenv('PGWALL_TEST_INTEGRATION_TEST') is not None, SKIP_REASON)
class TestIntegrationPgwall_test(unittest.TestCase):
    """Tests for `pgwall_test` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_something(self):
        """Tests parse arguments"""
        self.assertEqual(1, 1)
