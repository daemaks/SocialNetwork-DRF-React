from rest_framework import permissions


class IsOwnerAndAdminOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.method == "DELETE":
            return obj.username == request.user or request.user.is_staff

        # Instance must have an attribute named `owner`.
        return obj.username == request.user
