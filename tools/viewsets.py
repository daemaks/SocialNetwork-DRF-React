from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class MixedPermision:
    """Mixin permissions for actions"""

    def get_permissions(self):
        try:
            return [
                permission()
                for permission in self.permission_classes_by_action[
                    self.action
                ]
            ]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class UpgradedModelViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    MixedPermision,
    GenericViewSet,
):
    pass
