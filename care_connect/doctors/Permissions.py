from rest_framework.permissions import BasePermission

class IsAdminUserOrReadOnly(BasePermission):

    def has_permission(self, request, view):

        if request.method == "GET":
            return request.user.is_authenticated

        return request.user.is_authenticated and request.user.is_superuser
#NO NEED OF OBJECT PERMISSION
    # def has_object_permission(self, request, view, obj):
    #
    #     if request.method == "GET":
    #         return request.user.is_authenticated
    #
    #     return request.user.is_authenticated and request.user.is_superuser