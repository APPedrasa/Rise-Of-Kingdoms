from rok.models.Speedup import Speedup
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from rok.serializers import speedup_serializer

__all__= ['SpeedupGet']

class SpeedupGet(APIView):
    permission_classes=(AllowAny,)
    

    def get(self,request):
        id=request.GET.get('id')
        if id==None:
            
            query=Speedup.objects.all().values(
                'id', 
                'building_speedup', 
                'bquantity', 
                'traing_speedup', 
                'tquantity',
                'research_speedup', 
                'rquantity',
                'healing_speedup',
                'hquantity',
                'universal_speedup',
                'uquantity',
                )
            return Response(query)

        else:
            query=Speedup.objects.all().values(
                'id', 
                'building_speedup', 
                'bquantity', 
                'traing_speedup', 
                'tquantity',
                'research_speedup', 
                'rquantity',
                'healing_speedup',
                'hquantity',
                'universal_speedup',
                'uquantity',
                ).filter(id=id)
            return Response(query)
        
    # def get(self,request):
    #     query=Speedup.objects.all()
    #     serializer=speedup_serializer(query, many=True)
    #     return Response(serializer.data)
    
    def post(self,request):
        print(request.data)
        serializer=speedup_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.errors)
    
    def put(self,request):
        id=request.GET.get('id')
        speedup_object = Speedup.objects.get(id=id) 
        data = request.data

        speedup_object.building_speedup = data["building_speedup"]
        speedup_object.bquantity = data["bquantity"]
        speedup_object.traing_speedup = data["traing_speedup"]
        speedup_object.tquantity = data["tquantity"]
        speedup_object.research_speedup = data["research_speedup"]
        speedup_object.rquantity = data["rquantity"]
        speedup_object.healing_speedup = data["healing_speedup"]
        speedup_object.hquantity = data["hquantity"]
        speedup_object.universal_speedup = data["universal_speedup"]
        speedup_object.uquantity = data["uquantity"]
        speedup_object.save()

        serializer = speedup_serializer(speedup_object)
        return Response(serializer.data)