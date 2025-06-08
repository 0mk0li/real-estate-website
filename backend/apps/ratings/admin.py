from django.contrib import admin
from .models import Ratings

# Register your models here.


class RatingAdmin(admin.ModelAdmin):
    list_display = ["rater", "agent", "ratings"]


admin.site.register(Ratings, RatingAdmin)
