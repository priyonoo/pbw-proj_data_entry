from django import forms
from .models import Pengguna
from .models import Content
STATES = (
    ('', 'Choose...'),
    ('DKI   ','Daerah khusus Ibu Kota'),
    ('DIY','Daerah Istimewa Yogyakarta'),
    ('JABAR','Jawa Barat'),
)


class AddressForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    address_1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': '1234 Main St'})
    )
    address_2 = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'})
    )
    city = forms.CharField()
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)

class PenggunaForm(forms.ModelForm):
    state = forms.ChoiceField(choices=STATES)
    
    class Meta:
        model = Pengguna
        exclude = ["Tanggal join",]

class ContentForm(forms.ModelForm):
    class Meta :
        model = Content
        exclude = ["date_created"]