#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pgwall_test` package."""
import os
import tempfile
import shutil

import unittest
from pgwall_test.runner import PgwalltestRunner


class TestPgwalltestrunner(unittest.TestCase):
    """Tests for `pgwall_test` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_constructor(self):
        """Tests constructor"""
        myobj = PgwalltestRunner(outdir='foo', exitcode=0)

        self.assertIsNotNone(myobj)

    def test_run(self):
        """ Tests run()"""
        temp_dir = tempfile.mkdtemp()
        try:
            myobj = PgwalltestRunner(outdir=os.path.join(temp_dir, 'foo'),
                                                         exitcode=4)
            self.assertEqual(4, myobj.run())
        finally:
            shutil.rmtree(temp_dir)
