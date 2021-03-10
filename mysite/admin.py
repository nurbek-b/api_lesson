
from django.contrib import admin
from .models import Company, Advertisement, AdImage


class AdImageInline(admin.TabularInline):
    model = AdImage
    fields = ('image', 'description')
    max_num = 10
    min_num = 1

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    inlines = [AdImageInline,]


admin.site.register(Company)