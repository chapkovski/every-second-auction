from channels.routing import route
from consumers import ws_message, ws_connect, ws_disconnect
from otree.channels.routing import channel_routing
from channels.routing import include, route_class
print("TEST ROUTING")
# startwp_channel_name = r'^/group(?P<group_pk>\w+)$'
# customwp_routing = [route("websocket.connect",
#                  ws_connect,  path=startwp_channel_name),
#                  route("websocket.receive",
#                        ws_message,  path=startwp_channel_name),
#                  route("websocket.disconnect",
#                        ws_disconnect,  path=startwp_channel_name), ]
# channel_routing += [
#     include(customwp_routing, path=r"^/price_increase"),
# ]

#
#
#

# startwp_channel_name = r'^/group(?P<group_pk>\w+)$'
customwp_routing = [route("websocket.connect",
                 ws_connect),
                 route("websocket.receive",
                       ws_message),
                 route("websocket.disconnect",
                       ws_disconnect), ]
channel_routing += [
    include(customwp_routing, path=r"^/price_increase"),
]
