from rest_framework import mixins,generics,viewsets

from app.models import Movie
from app.serializers import MovieSerializer

#API VIEW FOR LISTING AND CREATING MOVIE RECORD

class MovieListCreate(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):
    queryset =Movie.objects.all()
    serializer_class = MovieSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)

#API VIEW FOR READ/UPDATE/DELETE EXISTING MOVIE RECORD

class MovieRetriveUpdateDelete(mixins.RetrieveModelMixin,
                               mixins.UpdateModelMixin,
                               mixins.DestroyModelMixin,
                               generics.GenericAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    def get(self,request,pk):
        return self.retrieve(request,pk)
    def put(self,request,pk):
        return self.update(request,pk)
    def patch(self,request,pk):
        return self.partial_update(request,pk)
    def delete(self,request,pk):
        return self.destroy(request.pk)


