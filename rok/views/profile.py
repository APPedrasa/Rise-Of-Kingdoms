from rok.models.Profile import Profile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from rok.serializers import profile_serializer

__all__= ['ProfileGet']

class ProfileGet(APIView):
    permission_classes=(AllowAny,)
    

    def get(self,request):
        id=request.GET.get('id')
        if id==None:
            
            query=Profile.objects.all().values(
                'id', 
                'governor_name', 
                'governor_id', 
                'power', 
                'kill_points',
                'civilization',
                'kingdom',
                'alliance', 
                )
            return Response(query)

        else:
            query=Profile.objects.all().values(
                'id', 
                'governor_name', 
                'governor_id', 
                'power', 
                'kill_points',
                'civilization'
                'kingdom',
                'alliance', 
                ).filter(id=id)
            return Response(query)
        
    # def get(self,request):
    #     query=Profile.objects.all()
    #     serializer=profile_serializer(query, many=True)
    #     return Response(serializer.data)
    
    def post(self,request):
        print(request.data)
        serializer=profile_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.errors)
    
    def put(self,request):
        id=request.GET.get('id')
        profile_object = Resource.objects.get(id=id) 
        data = request.data

        profile_object.governor_name = data["governor_name"]
        profile_object.governor_id = data["governor_id"]
        profile_object.power = data["power"]
        profile_object.kill_points = data["kill_points"]
        profile_object.civilization = data["civilization"]
        profile_object.kingdom = data["kingdom"]
        profile_object.alliance = data["alliance"]
        profile_object.save()

        serializer = profile_serializer(profile_object)
        return Response(serializer.data)