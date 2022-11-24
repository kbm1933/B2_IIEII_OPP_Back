from rest_framework import serializers
from users.models import User
from oilpainting.models import Image
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from oilpainting.serializers import ArticleListSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):   
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username

        return token



class UserprofileSerializer(serializers.ModelSerializer):

    # 내가 작성한 게시글 보기
    article_set = ArticleListSerializer(many=True)

    # 내가 좋아요 한 게시글 보기
    liked_article = ArticleListSerializer(many=True)

    class Meta:
        model = User
        fields = ("username", 'profile_img', 'article_set', 'liked_article')


class UserprofileImageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('profile_img',)