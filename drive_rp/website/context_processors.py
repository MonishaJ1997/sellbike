from .models import SiteLogo

def site_logo(request):
    logo = SiteLogo.objects.filter(is_active=True).first()
    return {"site_logo": logo}



from .models import FooterLogo, FooterBike, SocialIcon

def footer_context(request):
    return {
        "footer_logo": FooterLogo.objects.filter(is_active=True).first(),
        "footer_bike": FooterBike.objects.filter(is_active=True).first(),
        "social_icons": SocialIcon.objects.filter(is_active=True),
    }
