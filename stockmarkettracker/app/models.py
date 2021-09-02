from django.db import models

# Create your models here.
class stocks(models.Model):
    date        = models.DateTimeField()
    stock       = models.CharField(blank=True, max_length=128)
    ticker      = models.CharField(blank=True, max_length=128)
    closePrice  = models.FloatField(null=True)
    openPrice   = models.FloatField(null=True)
    lowPrice    = models.FloatField(null=True)
    volume      = models.FloatField(null=True)
    day_1_diff  = models.FloatField(null=True)
    day_5_diff  = models.FloatField(null=True)
    day_7_diff  = models.FloatField(null=True)
    month_1_diff = models.FloatField(null=True)
    month_3_diff = models.FloatField(null=True)
    month_6_diff = models.FloatField(null=True)
    year_1_diff = models.FloatField(null=True)

    class Meta:
        unique_together = (("date", "ticker"),)