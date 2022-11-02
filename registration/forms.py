from django.forms import ModelForm
from registration.models import Company

class CompanyRegistrationForm(ModelForm):
    class Meta:
        model = Company
        fields = '__all__'