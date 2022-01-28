from rok.models.Boost import Boost
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from rok.serializers import boost_serializer

__all__= ['BoostGet']

class BoostGet(APIView):
    permission_classes=(AllowAny,)
    

    def get(self,request):
        id=request.GET.get('id')
        if id==None:
            
            query=Boost.objects.all().values(
                'id', 
                'expanded_training', 
                'peace_shield', 
                'enhanced_gathering', 
                'enhanced_attack', 
                'enhanced_defense',
                'anti_reconnaissance_technology',
                'deceptive_troops',
                'army_expansion',
                'food_boost',
                'wood_boost',
                'stone_boost',
                'gold_boost',
                )
            return Response(query)

        else:
            query=Boost.objects.all().values(
                'id', 
                'expanded_training', 
                'peace_shield', 
                'enhanced_gathering', 
                'enhanced_attack', 
                'enhanced_defense',
                'anti_reconnaissance_technology',
                'deceptive_troops',
                'army_expansion',
                'food_boost',
                'wood_boost',
                'stone_boost',
                'gold_boost',
                ).filter(id=id)
            return Response(query)
        
    # def get(self,request):
    #     query=Boost.objects.all()
    #     serializer=boost_serializer(query, many=True)
    #     return Response(serializer.data)
    
    def post(self,request):
        print(request.data)
        serializer=boost_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.errors)
    
    def put(self,request):
        id=request.GET.get('id')
        boost_object = Boost.objects.get(id=id) 
        data = request.data

        boost_object.expanded_training = data["expanded_training"]
        boost_object.peace_shield = data["peace_shield"]
        boost_object.enhanced_gathering = data["enhanced_gathering"]
        boost_object.enhanced_attack = data["enhanced_attack"]
        boost_object.enhanced_defense = data["enhanced_defense"]
        boost_object.anti_reconnaissance_technology = data["anti_reconnaissance_technology"]
        boost_object.deceptive_troops = data["deceptive_troops"]
        boost_object.army_expansion = data["army_expansion"]
        boost_object.food_boost = data["food_boost"]
        boost_object.wood_boost = data["wood_boost"]
        boost_object.stone_boost = data["stone_boost"]
        boost_object.gold_boost = data["gold_boost"]
          
        boost_object.save()

        serializer = boost_serializer(boost_object)
        return Response(serializer.data)