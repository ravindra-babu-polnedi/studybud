from django.contrib import admin

# Register your models here.
from .models import Room,Topic,Message
class RoomAdmin(admin.ModelAdmin):
    list_display=['host','topic']

admin.site.register(Room,RoomAdmin)
admin.site.register(Topic)
admin.site.register(Message)