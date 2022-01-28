from rok.models.Commander import Commander
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from rok.serializers import commander_serializer

__all__= ['CommanderGet']

class CommanderGet(APIView):
    permission_classes=(AllowAny,)
    

    def get(self,request):
        id=request.GET.get('id')
        if id==None:
            
            query=Commander.objects.all().values(
                'id', 
                'commander', 
                'rarity', 
                'rokclass', 
                'star_level', 
                'specialty1',
                'specialty2',
                'specialty3',
                )
            return Response(query)

        else:
            query=Commander.objects.all().values(
                'id', 
                'commander', 
                'rarity', 
                'rokclass', 
                'star_level', 
                'specialty1',
                'specialty2',
                'specialty3',
                ).filter(id=id)
            return Response(query)
        
    # def get(self,request):
    #     query=Commanders.objects.all()
    #     serializer=commander_serializer(query, many=True)
    #     return Response(serializer.data)
    
    def post(self,request):
        print(request.data)
        serializer=commander_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.errors)
    
    def put(self,request):
        id=request.GET.get('id')
        commanders_object = Commander.objects.get(id=id) 
        data = request.data

        commanders_object.commander = data["commander"]
        commanders_object.rarity = data["rarity"]
        commanders_object.rokclass = data["rokclass"]
        commanders_object.star_level = data["star_level"]
        commanders_object.specialty1 = data["specialty1"]
        commanders_object.specialty2 = data["specialty2"]
        commanders_object.specialty3 = data["specialty3"]
          
        commanders_object.save()

        serializer = commander_serializer(commanders_object)
        return Response(serializer.data)