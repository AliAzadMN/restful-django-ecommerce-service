from djoser.serializers import UserSerializer as DjoserUserSerializer
from djoser.serializers import UserCreatePasswordRetypeSerializer


class UserSerializer(DjoserUserSerializer):
    class Meta(DjoserUserSerializer.Meta):
        fields = ['id', 'email', 'is_superuser', 'is_staff', 'date_joined', ]


class UserAdminCreateSerializer(UserCreatePasswordRetypeSerializer):
    class Meta(UserCreatePasswordRetypeSerializer.Meta):
        fields = ['email', 'is_staff', 'password', ]
