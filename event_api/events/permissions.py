#ONLY AUTHENTICATED USER CAN ACCESS THE VIEW
#ONLY ORGANIZER USER CAN CREATE A NEW EVENT
from rest_framework.permissions import BasePermission
class IsOrganizerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':#ANY LOGGED IN USER CAN READ REOCRDS
            return True
        return request.user.is_authenticated and request.user.roles=='organizer'#ONLY ORGANIZER CAN
    #OTHER OPERATIONS
#ONLY ORGANIZER OF THE EVENT CAN PERFORM UPDATION/DELETEION
    def has_object_permission(self,request,view,obj):
        if request.method=="GET":
            return request.user.is_authenticated #ANY LOGGED IN USER CAN READ
        return obj.organizer==request.user#BUT ONLY ORGANIZER OF THE EVENT CAN PERFORM DELETION/UPDATION