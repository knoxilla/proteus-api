from suds.client import Client
from suds.transport.https import HttpAuthenticated
from urllib2.request import HTTPSHandler
import ssl

class CustomTransport(HttpAuthenticated):

    def u2handlers(self):

        # use handlers from superclass
        handlers = HttpAuthenticated.u2handlers(self)

        # create custom ssl context, e.g.:
        ctx = ssl.create_default_context(cafile="/path/to/ca-bundle.pem")
        # configure context as needed...
        ctx.check_hostname = False

        # add a https handler using the custom context
        handlers.append(HTTPSHandler(context=ctx))
        return handlers

# instantiate client using this transport
c = Client("https://example.org/service?wsdl", transport=CustomTransport())
