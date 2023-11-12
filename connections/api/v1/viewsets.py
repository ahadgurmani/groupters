from rest_framework import viewsets,status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from connections.api.v1.serializers import ConnectionRequestSerializer
from connections.models import ConnectionRequests


class ConnectionRequestsViewset(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def create(self,request,*args,**kwargs):
        connection_to = request.data.get('connection_to')
        connection_by = request.data.get('connection_by')
        already = ConnectionRequests.objects.filter(connection_to=connection_to,connection_by= connection_by).exists()
        if already:
            return Response({"msg":'request already exists'})
        serializer = ConnectionRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg': 'Request has been sent'})


    @action(detail=True, methods=['GET'])
    def accept(self, request, pk=None):
        accept = ConnectionRequests.objects.filter(id =pk)
        if accept:
            accept.update(connection_status='Accept')
            return Response({"msg": 'request approved'})
        else:
            return Response({'msg':'id does not exist'}, status=status.HTTP_404_NOT_FOUND)



    @action(detail=True, methods=['GET'])
    def delete(self, request, pk=None):
        request = ConnectionRequests.objects.filter(id = pk)
        if request:
            request.delete()
            return Response({'msg':'request declined'})
        else:
            return Response({'msg': 'id does not exist'}, status=status.HTTP_404_NOT_FOUND)




# pending requests list for requested user

class PendingRequestsForRequestedUser(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def list(self, request,*args,**kwargs):
        list = ConnectionRequests.objects.filter(connection_to=request.user, connection_status='Pending')
        serializer = ConnectionRequestSerializer(list, many=True)
        return Response(serializer.data)




# Accepted requests list for requested user

class AcceptedRequestsForRequestedUser(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def list(self, request,*args,**kwargs):
        list = ConnectionRequests.objects.filter(connection_to=request.user, connection_status='Accept')
        serializer = ConnectionRequestSerializer(list, many=True)
        return Response(serializer.data)







# other user(friend) accepted requests list


class OtherUserAcceptedConnections(viewsets.ViewSet):
    def list(self,request,*arg,**kwargs):
        user_id = self.request.query_params.get('user')
        list = ConnectionRequests.objects.filter(connection_to=user_id, connection_status='Accept')
        serializer = ConnectionRequestSerializer(list, many=True)
        return Response(serializer.data)
