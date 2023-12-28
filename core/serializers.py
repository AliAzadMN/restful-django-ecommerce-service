from djoser.serializers import UserSerializer as DjoserUserSerialzier


class UserSerializer(DjoserUserSerialzier):
    class Meta(DjoserUserSerialzier.Meta):
        fields = ['id', 'email', 'is_superuser', 'is_staff', 'date_joined', ]
