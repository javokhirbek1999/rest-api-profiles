from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Users HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLS',
        ]    

        return Response({'message': 'Hello!', 'an_apiview': an_apiview,})

    def post(self,request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # PUT request replaces the initial object with the passed object
    def put(self,request,pk=None):
        """Handle updating an object"""
        return Response({'message':'PUT'})
    
    # Updates the object with passed data (does not replaces the initial object)
    def patch(self,request,pk=None):
        """Handle a partial update of an object"""
        return Response({'method':'PATCH'})
    
    def delete(self,request,pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})    

class PopulationData(APIView):
    """Test API View"""
    serializer_class = serializers.PopulationSerializer

    def get(self,request,format=None):
        welcome = ["Welcome"]
        return Response({'message':welcome})
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            country = serializer.validated_data.get('country')
            population = serializer.validated_data.get('population')
            year = serializer.validated_data.get('year')
            stats = {'Country': country,
                    'Population': population,
                    'Year': year}
            return Response({'data':stats})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk=None):
        return Response({'message':'PUT'})
    
    def patch(self,request,pk=None):
        return Response({'message':'PATCH'})
    
    def delete(self,request,pk=None):
        return Response({'message':'DELETE'})



