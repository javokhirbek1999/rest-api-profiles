from re import search
from rest_framework import views
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

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


class Job(APIView):
    """Test API View"""
    serializer_class = serializers.Jobs

    def get(self,request,format=None):
        api_demo_view = {
            'Message':'Welcome'
            }   
        return Response(api_demo_view)
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            title = serializer.validated_data.get('title')
            position = serializer.validated_data.get('position')
            company = serializer.validated_data.get('company')
            location = serializer.validated_data.get('location')
            salary = serializer.validated_data.get('salary')
            general = {"Title": title + " - " + position, 
                       "Company": company,
                        "Location": location,
                        "Salary": salary}
            return Response({'job':general})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request):
        return Response({'method':'PUT'})

    def patch(self,request):
        return Response({'method':'PATCH'})

    def delete(self,request):
        return Response({'method':'DELETE'})      



class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """Return a hello message"""

        a_viewset = [
            'Use actions (list, create, retrieve, update, partial-update)',
            'Automatically map to urls using Routes',
            'Provide more functionality with less code',
        ]

        return Response({'message':'Hello!', 'a_viewset':a_viewset})
    
    def create(self,request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}!"
            return Response({'message':message})
        else:
            return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method':'GET'})
    
    def update(self,request,pk=None):
        """Handle updating an object"""
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """Handle updating parts of an object"""
        return Response({'http_method':'PATCH'})
    
    def destroy(self,request,pk=None):
        """Handle removing an object"""
        return Response({'http_method':'DELETE'})

class DemoViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.Jobs

    def list(self,request):
        """Return a list of items"""   

        view_set = [
            'This is demo viewset that comes from django rest framework',
            'This is one of the convenient ways of building APIs',
            'ViewSet urls are mapped using Routes',
        ]

        return Response({'demo':view_set})
    
    def create(self,request,pk=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            title = serializer.validated_data.get('title')
            position = serializer.validated_data.get('position')
            company = serializer.validated_data.get('company')
            location = serializer.validated_data.get('location')
            salary = serializer.validated_data.get('salary')
            message = {
                'Title': title + ' - ' + position,
                'Company': company,
                'Location': location,
                'Salary': salary,
            }
            return Response(message)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self,request,pk=None):
        return Response({'http_method':'GET'})
    
    def update(self,request,pk=None):
        return Response({'http_method':'PUT'})
    
    def partial_update(self,request,pk=None):
        return Response({'http_method':'PATCH'})
    
    def delete(self,request,pk=None):
        return Response({'http_method':'DELETE'})
    
class CountriesData(viewsets.ViewSet):
    serializer_class = serializers.Counties

    def create(self,request,pk=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name');
            capital = serializer.validated_data.get('capital');
            population = serializer.validated_data.get('population');
            gdp = serializer.validated_data.get('gdp')
            message = {
                'Title': name,
                'Capital':capital,
                'Population':population,
                'gdp':gdp
            }
            return Response(message)
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

    def retrieve(self,request,pk=None):
        return Response({'message':'GET'})

    def update(self,request,pk=None):
        return Response({'message':'UPDATE'})
    
    def partial_update(self,request,pk=None):
        return Response({'message':'PATCH'})
    
    def delete(self,request,pk=None):
        return Response({'message':'DELETE'})
    

class Companies(viewsets.ViewSet):
    serializer_class = serializers.Companies


    def create(self,request,pk=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            hq_location = serializer.validated_data.get('hq_location')
            founded = serializer.validated_data.get('founded')
            revenue = serializer.validated_data.get('revenue')
            message = {
                'Comany':name,
                'Headquaters':hq_location,
                'Founded':founded,
                'Revenue':revenue
            }
            if message['Headquaters'] == 'Please select location':
                message.pop('Headquaters')
            return Response(message)
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
    def retrieve(self,request,pk=None):
        return Response({'message':'GET'})
    
    def partial_update(self,request,pk=None):
        return Response({'message':'PATCH'})
    
    def delete(self,request,pk=None):
        return Response({'message':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)


class UserLoginView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserAuthView(ObtainAuthToken):
    """Handles generating random authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserProfViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.CheckUpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)

