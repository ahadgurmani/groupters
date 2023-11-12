from django.urls import path,include
from rest_framework.routers import DefaultRouter

from connections.api.v1.viewsets import ConnectionRequestsViewset,PendingRequestsForRequestedUser,AcceptedRequestsForRequestedUser,OtherUserAcceptedConnections

routers = DefaultRouter()
routers.register('connection_request', ConnectionRequestsViewset, basename='request_connection')
routers.register('PendingRequests_For_RequestedUser', PendingRequestsForRequestedUser, basename='pendingsForRequestedUser')
routers.register('AcceptedRequests_For_RequestedUser', AcceptedRequestsForRequestedUser, basename='AcceptedForRequestedUser')
routers.register('AcceptedConnections_of_OtherUser', OtherUserAcceptedConnections, basename='AcceptedConnectionsOfOtherUser')






urlpatterns = [
    path("", include(routers.urls)),
]