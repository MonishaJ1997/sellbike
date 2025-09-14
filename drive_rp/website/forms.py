from django import forms
from django.core.validators import RegexValidator

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Name'
        })
    )
   
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email'}),
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
                message="Enter a valid email address."
            )
        ]
    )
    phone = forms.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^[6-9]\d{9}$',
                message="Phone number must be 10 digits and start with 6, 7, 8, or 9."
            )
        ],
        widget=forms.TextInput(attrs={
            'placeholder': 'Phone Number'
        })
    )
    reason = forms.ChoiceField(
    choices=[
        ('', 'Reason to Contact'),   # empty default (acts like placeholder)
        ('inquiry', 'Inquiry'),
        ('feedback', 'Feedback'),
        ('other', 'Other')
    ],
    widget=forms.Select(attrs={
        'required': 'required'
    })
)

    source = forms.ChoiceField(
    choices=[
        ('', 'How did you find out about us?'),  # empty default
        ('website', 'Website'),
        ('social', 'Social Media'),
        ('referral', 'Referral')
    ],
    widget=forms.Select(attrs={
        'required': 'required'
    })
)

    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Your Message',
            'rows':4
        })
    )
