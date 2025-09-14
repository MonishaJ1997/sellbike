from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def buy_bike(request):
    return render(request, "buy_bike.html")

def sell_bike(request):
    return render(request, "sell_bike.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def login_view(request):
    return render(request, "login.html")

# app/views.py
from django.shortcuts import render
from .models import Bike, BikeInfo
from .models import Feature
from .models import BikeCard
from .models import CompanyStats
from .models import Testimonial
from .models import BikeRider
  


def home(request):
    bikes = Bike.objects.all()
    infos = BikeInfo.objects.first()
    features = Feature.objects.all()
    
    bikesname = BikeCard.objects.all()
    company = CompanyStats.objects.first()
    testimonials = Testimonial.objects.all()
    rider = BikeRider.objects.first()
    
    return render(request, "home.html", {
        "bikes": bikes,
        "infos": infos,
        "features": features,
        "bikesname": bikesname,
        "company": company,
        "testimonials": testimonials,
        "rider": rider
    })


import json
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from .models import Banner, SellSection, HowItWorks, FastRider


def sell_bike(request):
    banners = Banner.objects.first()
    fast_rider = FastRider.objects.first()
    section = SellSection.objects.prefetch_related("cards__options").first()
    steps = HowItWorks.objects.all()

    # Build cards JSON
    cards_data = []
    if section:
        for c in section.cards.all():
            cards_data.append({
                "id": c.id,
                "name": c.name,
                "options": [{"id": o.id, "name": o.name} for o in c.options.all()]
            })

    return render(request, "sell_bike.html", {
        "banners": banners,
        "section": section,
        "steps": steps,
        "fast_rider": fast_rider,
        "cards_json": json.dumps(cards_data, cls=DjangoJSONEncoder),
    })




   


from django.shortcuts import render
from .models import About
from .models import Mission
from .models import ApproachImage

def about(request):
    about = About.objects.first() 
    mission = Mission.objects.first()
    images = {img.position: img for img in ApproachImage.objects.all()} # fetch first entry
    return render(request, "about.html", {
        "about": about,
        "mission": mission,
        "images": images,
    
    
    })

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import ContactMap

def contact(request):
    map_info = ContactMap.objects.first()  # fetch map info from DB

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Do something with form.cleaned_data if needed
            messages.success(request, "Message Sent Successfully!")
            return redirect("contact")
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form, "map_info": map_info})



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import LoginImage

def login_view(request):
    # Fetch first uploaded image (or None if empty)
    login_image = LoginImage.objects.first()

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")  # redirect to homepage

    return render(request, "login.html", {"login_image": login_image})

from django.shortcuts import render
from .models import FilterCard

def buy_bike(request):
    cards = FilterCard.objects.all()

    sort = request.GET.get("sort")
    if sort == "price_low":
        cards = cards.order_by("price")
    elif sort == "price_high":
        cards = cards.order_by("-price")
    elif sort == "km_low":
        cards = cards.order_by("kilometers")
    elif sort == "km_high":
        cards = cards.order_by("-kilometers")
    elif sort == "year_old":
        cards = cards.order_by("year")
    elif sort == "year_new":
        cards = cards.order_by("-year")
    else:  # newest first
        cards = cards.order_by("-id")

    return render(request, "buy_bike.html", {
        "cards": cards
    })


from django.shortcuts import render, get_object_or_404
from .models import BuyBike
from .models import BikeOverview
from .models import BookingStep
from .models import BikeSpecification


def buybike_detail(request, pk):
    cards = get_object_or_404(BuyBike, pk=pk)
    bike = BikeOverview.objects.get(pk=pk)
    steps = BookingStep.objects.all()
    spec = BikeSpecification.objects.first() 
    return render(request, "buybike_detail.html", {
        "cards": cards,
        "bike": bike,
        "steps": steps,
        "spec": spec
        })


# views.py
from .models import PaymentMethod
from .models import ConfirmationContent
    

def payment_page(request):
    payment_methods = PaymentMethod.objects.all()
    confirmation = ConfirmationContent.objects.last()
    
    context = {
        'subtotal': 3000,
        'gst_tax': 1000,
        'test_drive': 1000,
        'grand_total': 32000,
        'payment_methods': payment_methods,
        'confirmation': confirmation,
    }
    return render(request, 'payment_page.html', context)


