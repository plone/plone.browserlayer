# -*- coding: utf-8 -*-
from plone.browserlayer.testing import PLONEBROWSERLAYER_FUNCTIONAL_TESTING
from plone.testing import layered
import doctest
import unittest


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
            ),
            layer=PLONEBROWSERLAYER_FUNCTIONAL_TESTING
        )
    ])
