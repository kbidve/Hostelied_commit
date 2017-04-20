from django.contrib import admin
from .models import CotBasisRooms , FlatOnRent , Room_Amanities , Flat_Furnishing_Details
from leaflet.admin import LeafletGeoAdmin


class CotBasisRoomsAdmin(LeafletGeoAdmin):
    pass

admin.site.register(CotBasisRooms , CotBasisRoomsAdmin)
admin.site.register(FlatOnRent)
admin.site.register(Room_Amanities)
admin.site.register(Flat_Furnishing_Details)
