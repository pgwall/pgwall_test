#! /usr/bin/env python

import os
import time
import logging
from cellmaps_utils import logutils
from cellmaps_utils.provenance import ProvenanceUtil

import pgwall_test

logger = logging.getLogger(__name__)

def i_rule(x):
    print('Value of x ' + str(x))

class PgwalltestRunner(object):
    """
    Class to run algorithm
    """
    def __init__(self, outdir=None,
                 exitcode=None,
                 skip_logging=False,
                 input_data_dict=None):
        """
        Constructor

        :param exitcode: value to return via :py:meth:`.PgwalltestRunner.run` method
        :type int:
        """
        if outdir is None:
            raise PgwalltestError('outdir is None')

        self._outdir = os.path.abspath(outdir)
        self._exitcode = exitcode
        self._start_time = int(time.time())
        self._end_time = -1
        if skip_logging is None:
            self._skip_logging = False
        else:
            self._skip_logging = skip_logging
        self._input_data_dict = input_data_dict
        logger.debug('In constructor')

    def _write_task_start_json(self):
        """
        Writes task_start.json file with information about
        what is to be run

        """
        data = {}

        if self._input_data_dict is not None:
            data.update({'commandlineargs': str(self._input_data_dict)})

        logutils.write_task_start_json(outdir=self._outdir,
                                       start_time=self._start_time,
                                       version=pgwall_test.__version__,
                                       data=data)

    def _create_output_directory(self):
        """
        Creates output directory

        """
        if os.path.isdir(self._outdir):
            raise PgwalltestError(self._outdir + ' already exists')

        os.makedirs(self._outdir, mode=0o755)

    def run(self):
        """
        Runs pgwall_test


        :return:
        """
        exitcode = 99
        try:
            logger.debug('In run method')
            self._create_output_directory()
            self._write_task_start_json()
            return self._exitcode
        finally:
            self._end_time = int(time.time())
            if self._skip_logging is False:
                # write a task finish file
                logutils.write_task_finish_json(outdir=self._outdir,
                                                start_time=self._start_time,
                                                end_time=self._end_time,
                                                status=exitcode)


        return exitcode
