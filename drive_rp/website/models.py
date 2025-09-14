from django.db import models

# Create your models here.
# app/models.py


from django.db import models

class SiteLogo(models.Model):
    name = models.CharField(max_length=100, default="DriveRP Logo")
    image = models.ImageField(upload_to="logos/")  # will be stored in MEDIA/logos/
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name





from django.db import models

class Bike(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='bikes/')

    def __str__(self):
        return self.name

# app/models.py


class BikeInfo(models.Model):
    title = models.CharField(max_length=200)
    
    image = models.ImageField(upload_to="bike_info/")

    def __str__(self):
        return self.image


      # website/models.py

from django.db import models

class Feature(models.Model):
    ARROW_CHOICES = [
        ('down', 'Arrow Down'),
        ('up', 'Arrow Up'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='features/')  # requires Pillow installed
    arrow_direction = models.CharField(max_length=10, choices=ARROW_CHOICES, default='down')

    def __str__(self):
        return self.title

  
from django.db import models

class BikeCard(models.Model):
    title = models.CharField(max_length=200)   # Example: "Yamaha MT 15"
    year = models.IntegerField()               # Example: 2023
    engine_cc = models.CharField(max_length=50) # Example: "150CC BS6"
    km_driven = models.IntegerField()          # Example: 8700
    fuel_type = models.CharField(max_length=50, choices=[("Petrol", "Petrol"), ("Diesel", "Diesel")])
    owner = models.CharField(max_length=50)    # Example: "1st Owner"
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Example: 115000.00
    location = models.CharField(max_length=200, default="Tamil Nadu")

    image = models.ImageField(upload_to="bikesname/")

    def __str__(self):
        return f"{self.year} {self.title}"


from django.db import models

class CompanyStats(models.Model):
    title = models.CharField(max_length=200, default="Over 15000+ Satisfied Customers")
    logo = models.ImageField(upload_to="logos/", blank=True, null=True)

    def __str__(self):
        return self.title

class StatItem(models.Model):
    company = models.ForeignKey(CompanyStats, related_name="stats", on_delete=models.CASCADE)
    icon = models.CharField(max_length=100, help_text="Font Awesome class, e.g. fa-motorcycle") 
    value = models.CharField(max_length=50)   # Example: "5000+"
    label = models.CharField(max_length=100)  # Example: "Bike Purchased"

    def __str__(self):
        return f"{self.value} {self.label}"

from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    message = models.TextField()
    image = models.ImageField(upload_to="testimonials/")

    def __str__(self):
        return self.name

class Banner(models.Model):
    
    
    quote = models.TextField()
    background = models.ImageField(upload_to="banners/")

    def __str__(self):
        return f"Banner {self.id}"


from django.db import models
from django.utils.text import slugify

class SellSection(models.Model):
    title = models.CharField(max_length=120, default="Sell Fast By")
    subtitle = models.CharField(max_length=120, default="Enter Your Details")
    logo = models.ImageField(upload_to="sell/logo/", blank=True, null=True)
    background = models.ImageField(upload_to="sell/backgrounds/")

    def __str__(self):
        return self.title


class Card(models.Model):
    section = models.ForeignKey(SellSection, on_delete=models.CASCADE, related_name="cards")
    name = models.CharField(max_length=100)           # "Brand Name", "Model", etc.
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class CardOption(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name="options")
    name = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name



from django.db import models

class HowItWorks(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='how_it_works/')

    def __str__(self):
        return self.title




from django.db import models

class About(models.Model):
    title = models.CharField(max_length=200, default="About Us")
    image = models.ImageField(upload_to="about/")
    description = models.TextField()

    def __str__(self):
        return self.title


from django.db import models

class Mission(models.Model):
    title = models.CharField(max_length=100, default="Our Mission")
    description = models.TextField()
    background = models.ImageField(upload_to='mission/')
    
    def __str__(self):
        return self.title


from django.db import models

class ApproachImage(models.Model):
    image = models.ImageField(upload_to="approach/")
    position = models.CharField(
        max_length=20,
        choices=[
            ("top_left", "Top Left"),
            ("bottom_left_1", "Bottom Left 1"),
            ("bottom_left_2", "Bottom Left 2"),
            ("right_long", "Right Long"),
        ]
    )

    def __str__(self):
        return f"{self.position} - {self.image.url}"

from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    reason = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ContactMap(models.Model):
    title = models.CharField(max_length=100, default="Drive RP")
    map_image = models.ImageField(upload_to="maps/")  # store map as image in DB
    address = models.TextField()
    website = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.title




from django.db import models

class LoginImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="login/")

    def __str__(self):
        return self.title

from django.db import models

class FilterCard(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    engine_cc = models.CharField(max_length=50)
    kilometers = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=200, default="Tamil Nadu")
 
    image = models.ImageField(upload_to="bikes/")  # ✅ stores inside media/bikes/

    def __str__(self):
        return f"{self.year} {self.name}"



from django.db import models

class FooterLogo(models.Model):
    name = models.CharField(max_length=100, default="DriveRP Footer Logo")
    image = models.ImageField(upload_to="footer/logo/")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class FooterBike(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="footer/bikes/")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class SocialIcon(models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to="footer/social/")  # uploaded PNG/SVG icon
   
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


       



from django.db import models

class BuyBike(models.Model):
    name = models.CharField(max_length=100)        # e.g. "Susuki Access"
    year = models.IntegerField()                   # e.g. 2013
    kilometers = models.IntegerField()             # e.g. 2600
    owner = models.CharField(max_length=50)        # e.g. "3rd Owner"
    location = models.CharField(max_length=100)    # e.g. "Kanchipuram"
    image = models.ImageField(upload_to="buybike/")  # stored in media/buybike/
    
    def __str__(self):
        return f"{self.year} | {self.name}"


# models.py
from django.db import models

class PaymentMethod(models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='payment_icons/')
    
    def __str__(self):
        return self.name




class BikeRider(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="riders/")

    def __str__(self):
        return self.title



from django.db import models

class FastRider(models.Model):
    fast_rider_image = models.ImageField(upload_to="fastrider/")
    quote = models.TextField()

    def __str__(self):
        return self.quote[:50]


from django.db import models

class BikeOverview(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    variant = models.CharField(max_length=100)
    make_year = models.CharField(max_length=10)

    refurbished = models.CharField(max_length=10, default="No")
    rto_state = models.CharField(max_length=100)
    rto_city = models.CharField(max_length=100)
    registration_year = models.CharField(max_length=10, blank=True, null=True)

    kilometers = models.CharField(max_length=50)
    owners = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50)
    fuel_type = models.CharField(max_length=50)

    registration_certificate = models.CharField(max_length=10, default="No")
    finance = models.CharField(max_length=10, default="No")
    insurance = models.CharField(max_length=10, default="No")
    warranty = models.CharField(max_length=10, default="No")

    def __str__(self):
        return f"{self.brand} {self.model}"



from django.db import models

class BookingStep(models.Model):
    title = models.CharField(max_length=200)   # Example: "Choose Your Bike"
    description = models.CharField(max_length=255, blank=True, null=True)  # Optional
    image = models.ImageField(upload_to='steps/')  # upload images to media/steps/
    order = models.PositiveIntegerField(default=0)  # to control order of steps

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.order}. {self.title}"



from django.db import models

class BikeSpecification(models.Model):
    type = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    fuel_type = models.CharField(max_length=50)
    ignition_type = models.CharField(max_length=100)
    transmission_type = models.CharField(max_length=100)
    front_brake_type = models.CharField(max_length=100)
    rear_brake_type = models.CharField(max_length=100)
    abs = models.CharField(max_length=10, choices=[("Yes", "Yes"), ("No", "No")])
    odometer = models.CharField(max_length=100)
    wheel_type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.type} - {self.color}"


from django.db import models

class ConfirmationContent(models.Model):
    image = models.ImageField(upload_to='confirmation/')
    message_title = models.CharField(max_length=100, default='Booking Confirmed')
    message_text = models.CharField(max_length=200, default='The Bike is Yours – Enjoy Your Journey')

    def __str__(self):
        return self.message_title


