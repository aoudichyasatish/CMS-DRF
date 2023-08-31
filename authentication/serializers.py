from rest_framework import serializers
from .models import Usertable
from rest_framework.validators import UniqueValidator

class UsertableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usertable
        fields = ('email',)


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=Usertable.objects.all())]
            )
    password = serializers.CharField(required=True,min_length=8)
    full_name = serializers.CharField(required=True)
    phone = serializers.IntegerField(required=True)
    address = serializers.CharField()
    city = serializers.CharField()
    state = serializers.CharField()
    country = serializers.CharField()
    pincode = serializers.IntegerField(required=True)

    def create(self, validated_data):
        user = Usertable.objects.create(
            email = validated_data['email'],
            username = validated_data['email'],
            full_name = validated_data['full_name'],
            phone = validated_data['phone'],
            address = validated_data['address'],
            city = validated_data['city'],
            state = validated_data['state'],
            country = validated_data['country'],
            pincode = validated_data['pincode']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = Usertable
        fields = ('email', 'password', 'full_name', 'phone', 'address', 'city', 'state',
        'country', 'pincode')