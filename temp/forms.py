from django.forms import ModelForm
from temp.models import CompanyRegistration

class CompanyRegistrationForm(forms.Form):
    class Meta:
        model = CompanyRegistration
        fields = '__all__'