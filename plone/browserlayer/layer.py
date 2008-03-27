from zope.interface import directlyProvidedBy, directlyProvides
from zope.component import getAllUtilitiesRegisteredFor
from plone.browserlayer.interfaces import ILocalBrowserLayerType

def mark_layer(site, event):
    """Mark the request with all installed layers.
    """
    request = event.request
    layers = getAllUtilitiesRegisteredFor(ILocalBrowserLayerType)
    ifaces = list(layers) + list(directlyProvidedBy(request))
        
    # Since we allow multiple markers here, we can't use 
    # zope.publisher.browser.applySkin() since this filters out 
    # IBrowserSkinType interfaces, nor can we use alsoProvides(), since
    # this appends the interface (in which case we end up *after* the
    # default Plone/CMF skin)

    directlyProvides(request, *ifaces)

