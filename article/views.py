from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from article.models import Article
from article.serializers import ArticleSerializer


class article_list_view(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class article_detail_view(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field='slug'

class article_retrive_view(RetrieveAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
    lookup_field='id'

class article_create_view(ListCreateAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer

class article_retrive_update_destroy_view(RetrieveUpdateDestroyAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
    lookup_field='id'

# class article_update_view(RetrieveUpdateAPIView):
#     queryset=Article.objects.all()
#     serializer_class=ArticleSerializer
#     lookup_field='id'

# class article_destroy_view(RetrieveDestroyAPIView):
#     queryset=Article.objects.all()
#     serializer_class=ArticleSerializer
#     lookup_field='id'
