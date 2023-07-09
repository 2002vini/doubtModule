from channels.routing import ProtocolTypeRouter,URLRouter
import chat.routing
from channels.auth import AuthMiddlewareStack


# application=ProtocolTypeRouter({
#     'http':get_asgi_application(),
#    'websocket':AuthMiddlewareStack(
#         URLRouter(
#             chat.routing.websocket_urlpatterns
#         )
#     ),
#})