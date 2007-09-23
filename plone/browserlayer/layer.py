from zope.component import getAllUtilitiesRegisteredFor
from zope.publisher.browser import applySkin
from plone.browserlayer.interfaces import ILocalBrowserLayerType

def mark_layer(site, event):
    """Mark the request with all installed layers.
    """
    
    for layer in getAllUtilitiesRegisteredFor(ILocalBrowserLayerType):
        applySkin(event.request, layer)