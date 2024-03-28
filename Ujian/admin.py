from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import *

class BeritaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("title", "description", "image_tag",)
    search_fields = ("title",)
    list_filter = ("title",)

admin.site.register(Berita, BeritaAdmin)

class BukuTamuAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("nama", "email", "pesan",)
    search_fields = ("nama__startswith",)
    list_filter = ("nama",)

admin.site.register(BukuTamu, BukuTamuAdmin)
    
    
admin.site.site_header = "Admin Toko Buku"
admin.site.site_title = "Toko Buku"
admin.site.index_title = "Admin Malik"