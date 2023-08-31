from django.shortcuts import render
from rest_framework import generics, filters
from .models import Content
from .serializers import ContentSerializer

# Create your views here.

class ContentList(generics.ListAPIView):
    serializer_class = ContentSerializer
    def get_queryset(self):
        user=self.request.user
        if user.userrole == 'Author':
             queryset = Content.objects.filter(author=user.email)
             return queryset
        else:
            queryset = Content.objects.all()
            return queryset

class ContentDetail(generics.ListCreateAPIView):
    serializer_class = ContentSerializer

    def get_queryset(self):
        user=self.request.user
        if user.userrole == 'Author':
             queryset = Content.objects.filter(author=user.email)
             return queryset
        else:
            queryset = Content.objects.all()
            return queryset


class ContentSearchAPIView(generics.ListAPIView):
    search_fields = ['title', 'body', 'summary', 'category']
    filter_backends = (filters.SearchFilter,)
    queryset = Content.objects.all()
    serializer_class = ContentSerializer