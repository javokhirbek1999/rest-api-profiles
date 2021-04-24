from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self,request,format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Users HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLS',
        ]    

        return Response({'message': 'Hello!', 'an_apiview': an_apiview,})

class MoviesList(APIView):

    
    def get(self,request,format=None):
        """Returns the list of movies as an API"""
        movies = [
            {
                'name': 'Jobs',
                'year': 2016,
                'country': 'USA',
            },
            {
                'name': 'Silicon Valley',
                'year': 2014,
                'country': 'USA',
            },
            {
                'name': 'Born',
                'year': 2012,
                'country': 'USA',
            },
            
        ]

        return Response(movies)

    