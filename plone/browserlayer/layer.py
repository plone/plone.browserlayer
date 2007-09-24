from zope.interface import alsoProvides
from zope.component import getAllUtilitiesRegisteredFor
from plone.browserlayer.interfaces import ILocalBrowserLayerType

def mark_layer(site, event):
    """Mark the request with all installed layers.
    """
    
    for layer in getAllUtilitiesRegisteredFor(ILocalBrowserLayerType):
        alsoProvides(event.request, layer)