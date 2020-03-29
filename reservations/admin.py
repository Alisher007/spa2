from django.contrib import admin
from .models import Timelist, Room, Res

class ResAdmin(admin.ModelAdmin):
    list_display = ['pk',
                    'roomid',
                    'arrdate',
                    'starttime',
                    'endtime',
                    ]

# Register your models here.
admin.site.register(Timelist)
admin.site.register(Room)
admin.site.register(Res, ResAdmin)