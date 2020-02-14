from django.contrib import admin
from .models import slider, service, testimonials, photoupload, news


# Register your models here.
class sliderAdmin(admin.ModelAdmin):
    list_display = ('img', 'title')


class serviceAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')


class testimonialsAdmin(admin.ModelAdmin):
    list_display = ('img', 'desc', 'name')


class photoAdmin(admin.ModelAdmin):
    list_display = ("user", "photo", "caption", "caption_title")

class newsAdmin(admin.ModelAdmin):
    list_display = ("Name","Email","Telephone","Subject","Message")

admin.site.register(slider, sliderAdmin)
admin.site.register(service, serviceAdmin)
admin.site.register(testimonials, testimonialsAdmin)
admin.site.register(photoupload, photoAdmin)
admin.site.register(news, newsAdmin)
