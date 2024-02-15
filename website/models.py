from django.db import models
from django.utils import timezone

# Create your models here.
class Routes(models.Model):
    name_liv = models.CharField("Employees_name", max_length=100)
    Date = models.DateField("Date", default=timezone.now)
    ref_liv = models.CharField("Employees_ref", max_length=100, default="")
    new_Reg = models.CharField("city", max_length=100)
    Duration_TSP_minutes = models.IntegerField("Duration_TSP_minutes", default=0)
    Route_Length = models.FloatField("Route_TSP_Length", default=0.0)
    list_ref_clients = models.JSONField("list_ref_clients", default=list)
    list_name_clients = models.JSONField("list_name_clients", max_length=1000)
    URL_html = models.URLField("URL_html")

    def __str__(self):
        return self.name_liv