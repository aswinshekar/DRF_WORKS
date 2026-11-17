from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        #object level permission
        # if obj.user==request.user:
        #     return True
        if request.method=="GET":#any user can read
            return True
        return request.user==obj.user#only creator can update/delete

#condition obj.user==request.user means checks whether
#the creator of the object and the requested user is same
