from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from .forms import EmployeeSelectionForm
from .forms import EmployeeSelectionUrlForm
from .models import Routes

# Create your views here.
def home(request):
    return render(request, 'home.html', {})






def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']  # here message-name comes from contact.html file's input type name
        message_email = request.POST['message-email']
        message = request.POST['message']

        ### Send an Email Start ###
        send_mail(
            message_name, # subject
            message, # message
            message_email, # from email
            ['contact@valomnia.com','ikbel.fridhi@gmail.com',], # To email
        )
        ### Send an Email End ###

        return render(request, 'contact.html', {'message_name':message_name})

    else:
        return render(request, 'contact.html', {})

# def about(request):
#     return render(request, 'about.html', {})
def about(request):
    form = EmployeeSelectionForm()  # Instantiate the form
    return render(request, 'about.html', {'form': form})


def service(request):
    service = Service.objects.all()

    return render(request, 'service.html', {'service':service})

# def pricing(request):
#     return render(request, 'pricing.html', {})
def pricing(request):
    form = EmployeeSelectionUrlForm()  # Instantiate the form
    return render(request, 'pricing.html', {'form': form})


def appointment(request):
    if request.method == "POST":
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_schedule = request.POST['your-schedule']
        your_date = request.POST['your-date']
        your_message = request.POST['your-message']

        ### Send an Email Start ###
        appointment = "Name: " + your_name + " Phone: " + your_phone + " Email: " + your_email + " Address: " + your_address + " Schedule: " + your_schedule + " Date: " + your_date + " Message: " + your_message

        send_mail(
            'Appointment Request', # subject
            appointment, # message
            your_email, # from email
            ['omarfaruk2468@gmail.com'], # To email
            # ['omarfaruk2468@gmail.com','mehedibinhafiz@gmail.com'], # To email
        )
        ### Send an Email End ###

        return render(request, 'appointment.html', {
            'your_name':your_name,
            'your_phone':your_phone,
            'your_email':your_email,
            'your_address':your_address,
            'your_schedule':your_schedule,
            'your_date':your_date,
            'your_message': your_message
        })

    else:
        return render(request, 'home.html', {})


def booknow(request):
    return render(request, 'booknow.html')

########

def get_employee_dates(request):
    if request.method == 'POST':
        form = EmployeeSelectionForm(request.POST)
        if form.is_valid():
            employee_name = form.cleaned_data['employee_name']
            routes_data = Routes.objects.filter(name_liv=employee_name).values('Date', 'new_Reg')

            # Extracting data from routes_data
            dates_list = [str(route['Date']) for route in routes_data]
            city = routes_data[0]['new_Reg'] if routes_data else ''  # Assuming the city is the same for all entries

            return JsonResponse({'dates': dates_list, 'city': city})
    else:
        return JsonResponse({'error': 'Invalid request method'})





def get_employee_data(request):
    if request.method == 'POST':
        form = EmployeeSelectionUrlForm(request.POST)
        if form.is_valid():
            employee_name = form.cleaned_data['employee_name']
            selected_date = form.cleaned_data['selected_date']

            # Retrieve data based on employee_name and selected_date
            employee_data = Routes.objects.filter(name_liv=employee_name, Date=selected_date).values(
                'Duration_TSP_minutes', 'Route_Length', 'list_name_clients', 'URL_html'
            ).first()

            if employee_data:
                return JsonResponse({
                    'Duration_TSP_minutes': employee_data['Duration_TSP_minutes'],
                    'Route_Length': employee_data['Route_Length'],
                    'list_name_clients': employee_data['list_name_clients'],
                    'URL_html': employee_data['URL_html']
                })
            else:
                return JsonResponse({'error': 'Data not found for the specified employee and date'}, status=404)
        else:
            return JsonResponse({'error': 'Invalid form data'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)