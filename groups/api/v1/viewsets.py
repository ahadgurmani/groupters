from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from users.models import SignupUser
from .serializers import CreateGroupSerializer, AllGroupList_Serializer, Group_ProfileImgChangeSerializer, GroupEditSerializer
from rest_framework.response import Response
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


# viewset for create group
from ...models import CreateGroup


class CreateGroupViewset(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def create(self,request, *args, **kwargs):
        members = request.data.pop("members")[0].split(",")
        serializer = CreateGroupSerializer(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        group = CreateGroup.objects.filter(id=serializer.data["id"]).first()
        for i in members:
            group.members.add(int(i))
        return Response({'msg': 'Group Created Successfully'})



# viewset for list of all groups

class AllGroupList_Viewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = AllGroupList_Serializer
    queryset = CreateGroup.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['group_category__category', 'title', 'description']
    filterset_fields = ['group_category__category', 'group_Type']

# action for kick out a group member
    @action(detail=False, methods=['DELETE'])
    def remove_member(self, request):
        group_id = self.request.query_params.get('group_id')
        member_id = self.request.query_params.get('member_id')
        group = CreateGroup.objects.filter(id=group_id).first()
        member = group.members.filter(id=member_id).first()
        user = request.user
        if member:
            if group.admin.id == user.id:
                group.members.remove(member)
                return Response({'msg': f'you removed {member}'})
            return Response({'msg': 'only admin can remove member'})
        return Response({'msg': 'This member does not exist'})


# action when a group member leaves

    @action(detail=False, methods= ['DELETE'])
    def leave_group(self, request):
        group_id = self.request.query_params.get('group_id')
        member_id = self.request.query_params.get('member_id')
        group = CreateGroup.objects.filter(id=group_id).first()
        member = group.members.filter(id=member_id).first()
        user = request.user
        if member:
            if member.id == user.id:
                group.members.remove(member)
                return Response({'msg': f'{member}  has left the group'})
            return Response({'msg : admin have this command'})
        return Response({'msg': 'This member doest not exist'})











# viewset for requested user group list

class RequestedUserList(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def list(self,request):
        list = CreateGroup.objects.filter(admin=request.user)
        serializer = AllGroupList_Serializer(list, many=True)
        return Response(serializer.data)



# for request user joined groups


class RequestedUserJoined_Groups(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def list(self,request):
        list = CreateGroup.objects.filter(members=request.user)
        serializer = AllGroupList_Serializer(list, many=True)
        return Response(serializer.data)




# apis for group frofile image change and group edit

class GroupProfileImgChange_Viewset(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def update(self,request, pk=None):
        group_obj = CreateGroup.objects.filter(id=pk).first()
        serializer = Group_ProfileImgChangeSerializer(group_obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg': 'Image Updated successfully'})



class GroupEdit_Viewset(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def update(self,request, pk=None):
        group_obj = CreateGroup.objects.filter(id=pk).first()
        serializer = GroupEditSerializer(group_obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg': 'Changes Saved successfully'})
