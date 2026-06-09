from django.shortcuts import render, redirect
from .models import Member
from django.contrib import messages
from django.views.decorators.http import require_http_methods
# from django.contrib.auth import authenticate, login, get_user_model, logout

# User = get_user_model()
# Create your views here.
def welcomepage_view(request):
    return render(request, 'index.html')



def login_view(request):
    global employee
    # if request.user.is_authenticated:
    #      return redirect('home')
    
    if request.method == 'POST':
        Email = request.POST['email']
        Emp_Id = request.POST['emp_id']


        if Email and Emp_Id:
            try:
                employee = Member.objects.filter(Email=Email, Emp_Id=Emp_Id).first()
                request.session['Name'] = employee.Name
                request.session['Emp_Id'] = employee.Emp_Id
                request.session['Job'] = employee.Job
                request.session['Address'] = employee.Address
                return redirect('home')
            except Member.DoesNotExist:
                messages.error(request, "Invalid Credentials")
        else:
            messages.error(request, "Fill the fields")

        

    return render(request, 'login.html', )

def homepage_view(request):
    global employee
    if 'Emp_Id' not in request.session:
        return redirect('login')
    
    admin_email = Member.objects.get(Job="Admin")
    admin = Member.objects.get(Email=admin_email) 
    request.session['Announcements']  = admin.Announcements

    context = {
        'Name': request.session.get('Name'),
        'Emp_Id': request.session.get('Emp_Id'),
        'Job': request.session.get('Job'),
        'Address': request.session.get('Address'),
        'Announcements': request.session.get('Announcements'),
    }

    try:
        if request.method == 'POST':
            Complaints = request.POST['Complaints']
            Email = request.POST['email']

            employee = Member.objects.get(Email=Email)
            employee.Complaints = Complaints
            employee.save(update_fields=["Complaints"])

            messages.success(request, "Your complaint has been submitted successfully")
            return redirect("home")
    except:
        pass


    try:
        if request.method == 'POST':
            Leaves = request.POST['Leaves']
            Email = request.POST['email']

            employee = Member.objects.get(Email=Email)
            employee.Leaves = Leaves
            employee.save(update_fields=["Leaves"])

            messages.success(request, "Your leave request has been submitted successfully")
            return redirect("home")
    except:
        pass


    return render(request, 'home.html', context)




def logout_view(request):
    request.session.flush()
    return redirect('login')
