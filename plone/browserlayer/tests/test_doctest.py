# -*- coding: utf-8 -*-
from plone.browserlayer.testing import PLONEBROWSERLAYER_FUNCTIONAL_TESTING
from plone.testing import layered

import doctest
import re
import six
import unittest


class Py23DocChecker(doctest.OutputChecker):
    def check_output(self, want, got, optionflags):
        if six.PY2:
            want = re.sub('urllib.error.HTTPError', 'HTTPError', want)
        return doctest.OutputChecker.check_output(self, want, got, optionflags)


def test_suite():
    return unittest.TestSuite([
        layered(
            doctest.DocFileSuite(
                'README.rst',
                package='plone.browserlayer',
                optionflags=(
                    doctest.ELLIPSIS |
                    doctest.REPORT_ONLY_FIRST_FAILURE
                ),
                checker=Py23DocChecker(),
            ),
            layer=PLONEBROWSERLAYER_FUNCTIONAL_TESTING
        )
    ])
