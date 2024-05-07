from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from django.http import JsonResponse
from .models import spartanews
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import HttpResponse

# Create your views here.
@csrf_exempt
def sparta_news_list(request):
    if request.method == 'GET':
        news_list = spartanews.objects.all()
        serializer = PostSerializer(news_list, many=True)
        return JsonResponse(serializer.data, safe=False)

# 게시글 생성


@csrf_exempt
def sparta_news_create(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PostSerializer(data=data)
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
        serializer = PostSerializer(news)
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
        serializer = PostSerializer(news, data=data)
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
