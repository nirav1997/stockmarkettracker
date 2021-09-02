from django.contrib import admin
from app.models import stocks
# Register your models here.
@admin.register(stocks)
class stocksAdmin(admin.ModelAdmin):
    list_display = ("date", "stock", "ticker", "closePrice", "openPrice", "lowPrice", "volume")