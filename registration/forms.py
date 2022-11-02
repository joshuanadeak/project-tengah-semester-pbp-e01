from django.forms import ModelForm
from registration.models import CompanyRegistration

class CompanyRegistrationForm(ModelForm):
    class Meta:
        model = CompanyRegistration
        fields = '__all__'