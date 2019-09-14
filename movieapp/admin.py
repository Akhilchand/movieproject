from django.contrib import admin
from movieapp.models import *
#from djangoseo.admin import register_seo_admin
from django.contrib import admin
#from movieapp.seo import MetaAdd

#register_seo_admin(admin.site, MetaAdd)


class MovieAdmin(admin.ModelAdmin):
    list_display = ("movie_name", "category", "release_date")
    search_fields = ["movie_name"]
    list_filter = ["release_date"]


# Register your models here.
admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieDetail)
admin.site.register(MovieCategory)
admin.site.register(UserDetail)
admin.site.register(Songs)
admin.site.register(User_sel)
admin.site.register(Booking_info)
admin.site.register(Transaction)
admin.site.register(Seats)
admin.site.register(BookingTransactions)
