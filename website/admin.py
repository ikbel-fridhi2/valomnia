#from django.contrib import admin
#from .models import Routes

# Register your models here.

#admin.site.register(Routes)
import pandas as pd
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django import forms
from .models import Routes




class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()

class RoutesAdmin(admin.ModelAdmin):

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls
    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            csv_file = request.FILES["csv_upload"]

            # Assuming the first row is the header, adjust if needed
            df = pd.read_excel(csv_file)

            for index, row in df.iterrows():
                employees_name = row['Employees_name']
                date = row['Date']
                employees_ref = row['Employees_ref']
                city = row['city']
                duration_tsp_minutes = row['Duration_TSP_minutes']
                route_tsp_length = row['Route_TSP_Length']
                list_ref_clients = row['list_ref_clients']
                list_name_clients = row['list_name_clients']
                url_html = row['URL_html']

                # Check if any field is empty
                if any(pd.isnull(value) for value in
                       [employees_name, date, employees_ref, city, duration_tsp_minutes, route_tsp_length,
                        list_ref_clients, list_name_clients, url_html]):
                    print("Skipping row due to empty values:", row)
                    continue

                # Create a Routes instance and save it to the database
                route_instance, created = Routes.objects.update_or_create(
                    name_liv=employees_name,
                    Date=date,
                    ref_liv=employees_ref,
                    new_Reg=city,
                    Duration_TSP_minutes=duration_tsp_minutes,
                    Route_Length=route_tsp_length,  # Adjusted field name
                    list_ref_clients=list_ref_clients,
                    list_name_clients=list_name_clients,
                    URL_html=url_html,
                )

                print("Route instance saved:", route_instance)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)




admin.site.register(Routes, RoutesAdmin)
