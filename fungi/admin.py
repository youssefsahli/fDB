from django.contrib import admin
from .models import Genre, Fungi, FungiImage

class FungiImageInline(admin.TabularInline):
    model = FungiImage
    extra = 1

class FungiAdmin(admin.ModelAdmin):
    list_display = ('french_name', 'latin_name', 'edibility')
    list_filter = ('edibility',)
    search_fields = ('french_name', 'latin_name')
    fields = ('french_name', 'latin_name', 'edibility', 'smell', 'genre')
    inlines = [FungiImageInline]

admin.site.register(Genre)
admin.site.register(Fungi, FungiAdmin)
