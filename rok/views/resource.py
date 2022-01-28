from rok.models.Resource import Resource
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from rok.serializers import resource_serializer

__all__= ['ResourceGet']

class ResourceGet(APIView):
    permission_classes=(AllowAny,)
    

    def get(self,request):
        id=request.GET.get('id')
        if id==None:
            
            query=Resource.objects.all().values(
                'id', 
                'food', 
                'wood', 
                'stone', 
                'gold',
                'gems', 
                )
            return Response(query)

        else:
            query=Resource.objects.all().values(
                'id', 
                'food', 
                'wood', 
                'stone', 
                'gold',
                'gems', 
                ).filter(id=id)
            return Response(query)
        
    # def get(self,request):
    #     query=Resource.objects.all()
    #     serializer=resource_serializer(query, many=True)
    #     return Response(serializer.data)
    
    def post(self,request):
        print(request.data)
        serializer=resource_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.errors)
    
    def put(self,request):
        id=request.GET.get('id')
        resource_object = Resource.objects.get(id=id) 
        data = request.data

        resource_object.food = data["food"]
        resource_object.wood = data["wood"]
        resource_object.stone = data["stone"]
        resource_object.gold = data["gold"]
        resource_object.gems = data["gems"]
        resource_object.save()

        serializer = resource_serializer(resource_object)
        return Response(serializer.data)