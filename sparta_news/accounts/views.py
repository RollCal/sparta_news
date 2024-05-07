from rest_framework.response import Response
from rest_framework import status
from .serializers import AccountsSerializer
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from django.http import JsonResponse
from .models import spartanews
from .serializers import NewsSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import HttpResponse


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


@csrf_exempt
def sparta_news_list(request):
    if request.method == 'GET':
        news_list = spartanews.objects.all()
        serializer = NewsSerializer(news_list, many=True)
        return JsonResponse(serializer.data, safe=False)

# 게시글 생성


@csrf_exempt
def sparta_news_create(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NewsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

# 게시글 상세 조회


@csrf_exempt
def sparta_news_detail(request, pk):
    try:
        news = spartanews.objects.get(pk=pk)
    except spartanews.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = NewsSerializer(news)
        return JsonResponse(serializer.data)

# 게시글 수정


@csrf_exempt
def sparta_news_update(request, pk):
    try:
        news = spartanews.objects.get(pk=pk)
    except spartanews.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = NewsSerializer(news, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

# 게시글 삭제


@csrf_exempt
def sparta_news_delete(request, pk):
    try:
        news = spartanews.objects.get(pk=pk)
    except spartanews.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'DELETE':
        news.delete()
        return HttpResponse(status=204)
