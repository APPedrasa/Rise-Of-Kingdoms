from rok.models.Kill import Kill
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from rok.serializers import kill_serializer

__all__= ['KillGet']

class KillGet(APIView):
    permission_classes=(AllowAny,)
    

    def get(self,request):
        id=request.GET.get('id')
        if id==None:
            
            query=Kill.objects.all().values(
                'id', 
                'tier_1', 
                'tier_2', 
                'tier_3', 
                'tier_4',
                'tier_5',
                )
            return Response(query)

        else:
            query=Kill.objects.all().values(
                'id', 
                'tier_1', 
                'tier_2', 
                'tier_3', 
                'tier_4',
                'tier_5'
                ).filter(id=id)
            return Response(query)
        
    # def get(self,request):
    #     query=Kill.objects.all()
    #     serializer=kill_serializer(query, many=True)
    #     return Response(serializer.data)
    
    def post(self,request):
        print(request.data)
        serializer=kill_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.errors)
    
    def put(self,request):
        id=request.GET.get('id')
        kill_object = Kill.objects.get(id=id) 
        data = request.data

        kill_object.tier_1 = data["tier_1"]
        kill_object.tier_2 = data["tier_2"]
        kill_object.tier_3 = data["tier_3"]
        kill_object.tier_4 = data["tier_4"]
        kill_object.tier_5 = data["tier_5"]
        kill_object.save()

        serializer = kill_serializer(kill_object)
        return Response(serializer.data)