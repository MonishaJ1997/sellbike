
# Register your models here.
# app/admin.py
from django.contrib import admin
from .models import Bike

@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')

# app/admin.py

from .models import BikeInfo

@admin.register(BikeInfo)
class BikeInfoAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "image")



from .models import Feature

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'arrow_direction')
    list_filter = ('arrow_direction',)
    search_fields = ('title', 'description')


from .models import BikeCard

@admin.register(BikeCard)
class BikeCardAdmin(admin.ModelAdmin):
    list_display = ("title", "year", "engine_cc", "km_driven", "price")



from .models import CompanyStats, StatItem

class StatItemInline(admin.TabularInline):  # Inline editor for items
    model = StatItem
    extra = 1   # how many empty rows to show
    fields = ("icon", "value", "label")
    show_change_link = True

@admin.register(CompanyStats)
class CompanyStatsAdmin(admin.ModelAdmin):
    list_display = ("title",)
    inlines = [StatItemInline]

@admin.register(StatItem)
class StatItemAdmin(admin.ModelAdmin):
    list_display = ("value", "label", "company")
    list_filter = ("company",)



from .models import Testimonial

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "role")


from .models import Banner

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("quote", "background")




from .models import SellSection, Card, CardOption


class CardOptionInline(admin.TabularInline):
    model = CardOption
    extra = 3   # shows 3 empty rows by default


class CardAdmin(admin.ModelAdmin):
    list_display = ("name", "section", "order")
    inlines = [CardOptionInline]


class SellSectionAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle")


admin.site.register(SellSection, SellSectionAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(CardOption)


from .models import HowItWorks

admin.site.register(HowItWorks)



from .models import About

admin.site.register(About)

from django.contrib import admin
from .models import Mission

admin.site.register(Mission)


from django.contrib import admin
from .models import ApproachImage

admin.site.register(ApproachImage)



from django.contrib import admin
from .models import Contact, ContactMap

admin.site.register(Contact)
admin.site.register(ContactMap)


from django.contrib import admin
from .models import LoginImage

@admin.register(LoginImage)
class LoginImageAdmin(admin.ModelAdmin):
    list_display = ("title", "image")


from django.contrib import admin
from .models import FilterCard

@admin.register(FilterCard)
class FilterCardAdmin(admin.ModelAdmin):
    list_display = ("name", "year", "engine_cc", "kilometers", "fuel_type", "owner", "price")
    list_filter = ("year", "fuel_type", "owner")
    search_fields = ("name", "engine_cc")






from django.contrib import admin
from .models import SiteLogo

@admin.register(SiteLogo)
class SiteLogoAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active")
    list_editable = ("is_active",)



from django.contrib import admin
from .models import FooterLogo, FooterBike, SocialIcon

@admin.register(FooterLogo)
class FooterLogoAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active")

@admin.register(FooterBike)
class FooterBikeAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active")

@admin.register(SocialIcon)
class SocialIconAdmin(admin.ModelAdmin):
    list_display = ("name","icon", "is_active")



from django.contrib import admin
from .models import BuyBike

@admin.register(BuyBike)
class BuyBikeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "year", "location", "image")


# admin.py
from django.contrib import admin
from .models import PaymentMethod

admin.site.register(PaymentMethod)




from django.contrib import admin
from .models import BikeRider

@admin.register(BikeRider)
class BikeRiderAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "image")



from django.contrib import admin
from .models import FastRider

@admin.register(FastRider)
class FastRiderAdmin(admin.ModelAdmin):
    list_display = ("id", "quote", "fast_rider_image")
    search_fields = ("quote",)


from django.contrib import admin
from .models import BikeOverview

@admin.register(BikeOverview)
class BikeOverviewAdmin(admin.ModelAdmin):
    list_display = (
        "brand", "model", "variant", "make_year",
        "kilometers", "owners", "fuel_type", "insurance", "warranty"
    )
    search_fields = ("brand", "model", "variant", "rto_state", "rto_city")
    list_filter = ("fuel_type", "insurance", "warranty", "rto_state")


from django.contrib import admin
from .models import BookingStep

@admin.register(BookingStep)
class BookingStepAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)


from django.contrib import admin
from .models import BikeSpecification

@admin.register(BikeSpecification)
class BikeSpecificationAdmin(admin.ModelAdmin):
    list_display = (
        "type", "color", "fuel_type", "ignition_type",
        "transmission_type", "front_brake_type", "rear_brake_type",
        "abs", "odometer", "wheel_type",
    )

    from django.contrib import admin
from .models import ConfirmationContent

admin.site.register(ConfirmationContent)

