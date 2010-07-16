Introduction
============

This package aims to make it easier to register visual components (e.g. views
and viewlets) so that they only show up in a Plone site where they have been
explicitly installed.

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
