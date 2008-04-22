Introduction
============

This package aims to make it easier to register visual components (e.g. views
and viewlets) so that they only show up in a Plone site where they have been
explicitly installed.

It requires GenericSetup 1.4 later.

Basic usage
-----------

To use this feature, you should:

- declare plone.browserlayer as a dependency, e.g. in setup.py::

   install_requires=[
         'plone.browserlayer',
     ],

- ensure that its ZCML is loaded, e.g. with an include from your own package::

   <include package="plone.browserlayer" />
   
- create a layer marker interface unique to your product::

   from zope.interface import Interface
   class IMyProductLayer(Interface):
       """A layer specific to my product 
       """
       
- register this with GenericSetup, in a browserlayer.xml file::

   <layers>
       <layer name="my.product" 
              interface="my.product.interfaces.IMyProductLayer" />
   </layers>
   
- register visual components in ZCML for this layer, e.g.::

   <browser:page
       name="my-view"
       for="*"
       layer=".interfaces.IMyProductLayer"
       permission="zope.Public"
       template="my-view.pt"
       />

No seriously, it works, just look here
--------------------------------------

In testing.zcml we have registered a view, layer-test-view, available only for
the layer plone.browserlayer.tests.interfaces.IMyProductLayer.

Before the product is installed, we cannot view this:

    >>> from plone.browserlayer.tests.interfaces import IMyProductLayer
    >>> from plone.browserlayer import utils
    >>> IMyProductLayer in utils.registered_layers()
    False

    >>> from Products.Five.testbrowser import Browser
    >>> browser = Browser()
    >>> browser.open(self.portal.absolute_url() + '/@@layer-test-view')
    Traceback (most recent call last):
    ...
    HTTPError: HTTP Error 404: Not Found
    
We can view a view registered for the default layer, though:

    >>> browser.open(self.portal.absolute_url() + '/@@standard-test-view')
    >>> print browser.contents
    A standard view
    
However, if we install the product the interface is registered in the local
site manager. Here we use the utility method directly, though we could also
use GenericSetup.
    
    >>> utils.register_layer(IMyProductLayer, name='my.product')
    >>> IMyProductLayer in utils.registered_layers()
    True
    
And if we now traverse over the site root and render the view, it should be
there.

    >>> browser.open(self.portal.absolute_url() + '/@@layer-test-view')
    >>> print browser.contents
    A local view
    
Unlike when applying a new skin, layers installed in this way do not override
views registered for the default layer.

    >>> browser.open(self.portal.absolute_url() + '/@@standard-test-view')
    >>> print browser.contents
    A standard view
    
It is also possible to uninstall a layer:

    >>> IMyProductLayer in utils.registered_layers()
    True
    >>> utils.unregister_layer(name='my.product')
    >>> IMyProductLayer in utils.registered_layers()
    False
    
    >>> browser.open(self.portal.absolute_url() + '/@@layer-test-view')
    Traceback (most recent call last):
    ...
    HTTPError: HTTP Error 404: Not Found
    
GenericSetup support
--------------------

Most of the time, you will be registering layers using GenericSetup. Here
is how that looks.

    >>> from Products.CMFCore.utils import getToolByName
    >>> portal_setup = getToolByName(self.portal, 'portal_setup')

We should be able to install our product's profile. For the purposes of
this test, the profile is defined in tests/profiles/default/testing and 
registered in testing.zcml. It has a file called browserlayer.xml which
contains::

    <layers>
        <layer name="plone.browserlayer.tests" 
               interface="plone.browserlayer.tests.interfaces.IMyProductLayer" />
    </layers>

Let's import it:

    >>> IMyProductLayer in utils.registered_layers()
    False
    >>> _ = portal_setup.runAllImportStepsFromProfile('profile-plone.browserlayer:testing')
    >>> IMyProductLayer in utils.registered_layers()
    True

And just to prove that everything still works:

    >>> browser.open(self.portal.absolute_url() + '/@@layer-test-view')
    >>> print browser.contents
    A local view

    >>> browser.open(self.portal.absolute_url() + '/@@standard-test-view')
    >>> print browser.contents
    A standard view

