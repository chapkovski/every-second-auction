from channels.routing import route_class
from .consumers import PriceTracker

channel_routing = [
    route_class(PriceTracker, path=PriceTracker.url_pattern),

]
