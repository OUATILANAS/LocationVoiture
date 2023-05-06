from django.shortcuts import redirect, render
from django.http import HttpResponse
from app.forms import VoitureForm,ReservationForm
from app.models import Voiture,Reservation
from app.models import Agence


from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator

from faker import Faker
from django.contrib import messages

from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
import requests 
from bs4 import BeautifulSoup 

def get_title(request):
   
    if request.method == "POST":
        url = request.POST.get('url') # 👉️ Get URL from Input
        req = requests.get(url) # 👉️ Make request
        web_s = req.text # 👉️ Get The content of the request
        soup = BeautifulSoup(web_s, "html.parser") # 👉️ Parse 
        title = soup.title.string # 👉️ Get Value of Title tag

        return render(request, "scraptitle.html", {"title":title})

    return render(request, "scraptitle.html")

def home(request):
    cars = Voiture.objects.filter(IsAvailable=1)  # Fetch available cars
    voiture = Voiture.objects.all() 

    car_name = request.GET.get('car_name')
    selectedcar = Voiture.objects.filter(IsAvailable=1)
    return render(request, "index.html", {'cars': cars,'voiture': voiture,'selectedcar': selectedcar, 'car_name': car_name})


def About(request):
    return render(request,"about.html")

def BlogSingle(request):
    return render(request,"blog-single.html")
def Blog(request):
    return render(request,"blog.html")
def CarSingle(request, id):
    car = Voiture.objects.get(pk=id)
    context = {
        'car': car,
    }
    return render(request, 'car-single.html', context)
def Car(request):
    voiture = Voiture.objects.all()  
    paginator = Paginator(voiture, 3)  # Display 3 cars per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'car.html', {'page_obj': page_obj})
def Contact(request):
    if request.method == "POST": 
        message = request.POST['message'] 
        email = request.POST['email'] 
        name = request.POST['name'] 
        subject = request.POST['subject'] 
        send_mail(
            subject,
            message + '\n\nFrom: ' + name,
            'CarBook <your_email_address>',
            [email],
            fail_silently=False)

    return render(request,"contact.html")

    
def Pricing(request):
    return render(request,"pricing.html")
def Services(request):
    return render(request,"services.html")

def home3(request):
    return render(request,"test.html")


def products_list(request):
    return HttpResponse("Hello, World!")
# Create your views here.


@login_required(login_url='login')
def index2(request):
    voiture = Voiture.objects.all()  
    return render(request,"./car/show.html",{'Voiture':voiture})  

@login_required(login_url='login')
def addnew(request):
    if request.method == "POST":  
        form = VoitureForm(request.POST,request.FILES)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass
    else:  
        form = VoitureForm()  
    return render(request,'./car/index.html',{'form':form}) 

@login_required(login_url='login')
def edit(request, id):  
    voiture = Voiture.objects.get(id=id)  
    return render(request,'./car/edit.html', {'voiture':voiture}) 

@login_required(login_url='login')
def update(request, id):
    voiture = Voiture.objects.get(id=id)
    form = VoitureForm(request.POST or None,request.FILES, instance=voiture)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        agences = Agence.objects.all()
        return render(request, './car/edit.html', {'voiture': voiture, 'form': form, 'agences': agences, 'selected_agence': voiture.Agence})

    return render(request, './car/edit.html', {'voiture': voiture, 'form': form})

@login_required(login_url='login')
def delete(request, id):  
    voiture = Voiture.objects.get(id=id)  
    voiture.delete()  
    return redirect("/") 



@login_required(login_url='login')
def HomePage(request):
    return render (request,'./register/home.html')



def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('/user')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'./register/login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'./register/signup.html')

def rent_a_car(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            car = reservation.car
            pickup_date = reservation.pickup_date
            dropoff_date = reservation.dropoff_date

            if dropoff_date <= pickup_date:
                error_message = 'The drop-off date must be greater than the pick-up date.'
                messages.error(request, error_message)
                return redirect('/home')

            conflicting_reservations = Reservation.objects.filter(
                car=car,
                pickup_date__lte=dropoff_date,
                dropoff_date__gte=pickup_date
            )

            if conflicting_reservations.exists():
                error_message = 'This car is already reserved for the selected time period.'
                messages.error(request, error_message)
                return redirect('/home')

            reservation.save()
            return redirect('/home')
    else:
        form = ReservationForm()
        form.fields['car'].queryset = Voiture.objects.filter(IsAvailable=True)
                    
    error_message = 'Please fill all the fields.'

    messages.error(request, error_message)
    return redirect('/home')
