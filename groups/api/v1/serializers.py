from rest_framework import serializers

from GroupPosts.api.v1.serializers import GroupPostSerializer
# serializer for create group
from groups.models import CreateGroup, GroupCategory
from users.api.v1.serializers import SignupSerializer


class CreateGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateGroup
        fields = ['id', 'admin', 'image', 'group_Type', 'group_category', 'description','title']




# serializer for all groups list

class CategorySerializerForGroups(serializers.ModelSerializer):
    class Meta:
        model = GroupCategory
        fields = ['id', 'category']


class AllGroupList_Serializer(serializers.ModelSerializer):
    members = SignupSerializer(many=True, read_only=True)
    group_category = CategorySerializerForGroups(many=False, read_only=True)
    class Meta:
        model = CreateGroup
        fields = ['id', 'admin', 'image', 'group_Type', 'group_category', 'description', 'members', 'title']




# serializers for profile pic change and profile edit

class Group_ProfileImgChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateGroup
        fields = ['id', 'image']



class GroupEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateGroup
        fields = ['id', 'admin', 'image', 'group_Type', 'group_category', 'description','title']
