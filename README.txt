Introduction
============

This package makes it possible to register new browser layers, which are
automatically applied to the request when the appropriate product is installed.


Example
=======

First we must create an interface that will be used for the layer. This
is a trivial marker interface::

    from zope.interface import Interface

    class IMyProductLayer(Interface):
        """Browser layer indicating of MyProduct is installed in a site.
        """


This layer needs to be registered with plone.browserlayer. This is done
through a ''browserlayer.xml'' file in your package's GenericSetup profile:

    <layers>
     <layer
         name="MyProduct.
         interface="Products.MyuProduct.interfaces.IMyProductLayer"
         />
    </layers>


