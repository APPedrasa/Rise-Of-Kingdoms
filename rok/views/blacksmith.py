from rok.models.Blacksmith import Blacksmith
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from rok.serializers import blacksmith_serializer

__all__= ['BlacksmithGet']

class BlacksmithGet(APIView):
    permission_classes=(AllowAny,)
    

    def get(self,request):
        id=request.GET.get('id')
        if id==None:
            
            query=Blacksmith.objects.all().values(
                'id', 
                'leather', 
                'iron_ore', 
                'animal_bone', 
                'ebony', 
                )
            return Response(query)

        else:
            query=Resource.objects.all().values(
                'id', 
                'leather', 
                'iron_ore', 
                'animal_bone', 
                'ebony', 
                ).filter(id=id)
            return Response(query)
        
    # def get(self,request):
    #     query=Blacksmith.objects.all()
    #     serializer=blacksmith_serializer(query, many=True)
    #     return Response(serializer.data)
    
    def post(self,request):
        print(request.data)
        serializer=blacksmith_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.errors)
    
    def put(self,request):
        id=request.GET.get('id')
        resource_object = Blacksmith.objects.get(id=id) 
        data = request.data

        blacksmith_object.leather = data["leather"]
        blacksmith_object.iron_ore = data["iron_ore"]
        blacksmith_object.animal_bone = data["animal_bone"]
        blacksmith_object.ebony = data["ebony"]
        blacksmith_object.save()

        serializer = blacksmith_serializer(blacksmith_object)
        return Response(serializer.data)