
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, JsonResponse
from  rest_framework.parsers import JSONParser
from . models import Article, Profile
from . serializers import ArticleSerializer, ProfileSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework import viewsets

# Create your views here.


class ArticleViewSetModel(viewsets.ModelViewSet,):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class ArticleViewSets(viewsets.GenericViewSet,mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

class ArticleViewSet(viewsets.ViewSet):
    
    def list(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = ArticleSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
        
        
    def update(self, request, pk):
        article = Article.objects.get(pk=pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        article = Article.objects.get(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    










def index(request):
    return render(request, 'index.html')
'''
@csrf_exempt
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
@csrf_exempt   
def article_details(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status=201)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'GET':
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse(status=204)
'''

@api_view(['POST', 'GET'])
def article_list(request,):
    if request.method == 'GET':
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data,)
    elif request.method == 'POST':
       serializer = ArticleSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
@api_view(['GET', 'PUT', 'DELETE'])
def article_details(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data,)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    

class Generic(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class GenericDetails(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes  = [IsAuthenticated]
    
    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)
    
    
        
class ArticleAPIView(APIView):
    
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class Details(APIView):
    
    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
        
    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        article = self.get_objects(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
                    
