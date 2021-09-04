from django.contrib import admin
from app.models import stocks
# Register your models here.
@admin.register(stocks)
class stocksAdmin(admin.ModelAdmin):
    list_display = ("date", "stock", "ticker", "closePrice", "openPrice", "lowPrice", "volume",
                    "day_1_diff",
                    "day_5_diff",
                    "day_7_diff" ,
                    "month_1_diff",
                    "month_3_diff",
                    "month_6_diff",
                    "year_1_diff" )