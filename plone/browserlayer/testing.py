# -*- coding: utf-8 -*-
from plone.app.testing import PloneSandboxLayer
from plone.app.testing.layers import FunctionalTesting


class PloneBrowserlayerLayer(PloneSandboxLayer):

    def setUpZope(self, app, configurationContext):
        import plone.browserlayer.tests
        self.debug_mode = True
        self.loadZCML('tests/testing.zcml', package=plone.browserlayer)
        self.loadZCML(package=plone.browserlayer)
        self.debug_mode = False


PLONEBROWSERLAYER_FIXTURE = PloneBrowserlayerLayer()

PLONEBROWSERLAYER_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONEBROWSERLAYER_FIXTURE,),
    name="PloneBrowserlayer:Functional"
)
