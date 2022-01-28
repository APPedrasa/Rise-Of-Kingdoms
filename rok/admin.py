from django.contrib import admin

from rok.models.Commander import Commander
from rok.models.Resource import Resource
from rok.models.Blacksmith import Blacksmith
from rok.models.Profile import Profile
from rok.models.Speedup import Speedup
from rok.models.Boost import Boost
from rok.models.Kill import Kill

#Register your Models here.
admin.site.register(Commander)
admin.site.register(Resource)
admin.site.register(Blacksmith)
admin.site.register(Profile)
admin.site.register(Speedup)
admin.site.register(Boost)
admin.site.register(Kill)