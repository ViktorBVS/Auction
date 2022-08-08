from django.contrib import admin
from .models import Brend, Type, Sex, Case, Strap, Resist, Country, Product, Shop, Image, Watchlist, Comment, Stock

class ProductAdmin(admin.ModelAdmin):
    list_display = ['pr_Brend', 'pr_Name', 'pr_Type', 'pr_Sex', 'pr_Case', 'pr_Strap', 'pr_Resist', 'pr_Country']
    list_filter = ['pr_Brend', 'pr_Type', 'pr_Sex', 'pr_Case', 'pr_Strap', 'pr_Resist', 'pr_Country'] # фильтр
    
class ShopAdmin(admin.ModelAdmin):
    list_display = ['sh_Product', 'sh_Price', 'sh_Total', 'sh_Sales', 'sh_Left', 'sh_Status', 'sh_Sale', 'sh_Date']
    list_filter = ['sh_Status']                                                 # фильтр
    list_editable = ['sh_Price', 'sh_Total', 'sh_Sales', 'sh_Left', 'sh_Sale', 'sh_Status']            # что можно менять после создания объявления

admin.site.register(Brend)
admin.site.register(Type)
admin.site.register(Sex)
admin.site.register(Case)
admin.site.register(Strap)
admin.site.register(Resist)
admin.site.register(Country)
admin.site.register(Product, ProductAdmin)
admin.site.register(Shop, ShopAdmin)
admin.site.register(Image)
admin.site.register(Watchlist)
admin.site.register(Comment)
admin.site.register(Stock)
