from rest_framework.response import Response
from rest_framework import status, generics, permissions
from .serializers import AccountsSerializer
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from post.models import Comment
from .serializers import LikedCommentSerializer
from .serializers import LikedPostSerializer




class AccountListAPIView(APIView):
    def post(self, request):
        # 회원가입하기
        serializer = AccountsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # 비밀번호 암호화 처리하기
            data = serializer.data
            id = data.get('id')
            # 패스워드를 암호화하는 기능이 get_user_model안에 있다. , 방금 만든 유저 갖고오기
            user = get_user_model().objects.get(id=id)
            # 입력한 패스워드를 가져오고, set_password 메소드가 알아서 암호화를 해서 할당해준다
            user.set_password(request.data.get('password'))
            user.save()  # 조작한 데이터를 DB에 저장
            return Response(data, status=status.HTTP_201_CREATED)

class LikedCommentListView(generics.ListAPIView):
    serializer_class = LikedCommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return user.liked_comments.all()
    
class LikedPostListView(generics.ListAPIView):
    serializer_class = LikedPostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return user.liked_posts.all()
