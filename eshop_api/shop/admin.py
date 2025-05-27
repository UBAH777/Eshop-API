from django.contrib import admin
from django import forms

from .models import Category, Vendor, Item, ItemShots, Rating, RatingStar, Review
from django.utils.safestring import mark_safe

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ItemAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Item
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("id", "name")


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1
    readonly_fields = ("name", "email")


"""
class ItemShotsInline(admin.StackedInline):
    model = ItemShots
    extra = 1
"""


class ItemAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "url", "get_image")
    list_display_links = ("title", )
    list_filter = ("category", "year", "vendor")
    search_fields = ("title", "category__name")
    inlines = [ReviewInline, ] #ItemShotsInline
    save_on_top = True
    save_as = True
    form = ItemAdminForm

    readonly_fields = ("get_image", )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="50"')

    get_image.short_description = "Изображение"


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "parent", "item")
    list_display_links = ("id", )
    readonly_fields = ("name", "email")


class VendorAdmin(admin.ModelAdmin):
    list_display = ("title", "url")


class RatingAdmin(admin.ModelAdmin):
    list_display = ("star", "item", "ip")


"""
class ItemShotsAdmin(admin.ModelAdmin):
    list_display = ("title", "item")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
       return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Изображение"
"""


# admin.site.register(Category, CategoryAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(ItemShots, ) #ItemShotsAdmin
admin.site.register(Rating, RatingAdmin)
admin.site.register(Review, ReviewAdmin)

admin.site.register(RatingStar)


admin.site.site_title = "Eshop"
admin.site.site_header = "Eshop"
