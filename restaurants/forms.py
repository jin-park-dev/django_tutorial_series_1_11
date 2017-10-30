from django import forms

from .models import RestaurantLocation
from .validators import validate_categories, clean_email

class ResaurantCreateForm(forms.Form):
    name            = forms.CharField()
    location        = forms.CharField(required=False)
    category        = forms.CharField(required=False)

    #clean_something eg
    #clean_(name/location/category)
    #is called when "if form.is_valid" is called. So below code is validated for name (one of the ways)
    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == "Hello":
            raise forms.ValidationError("Not a valid name")
        return name

# This works with CreativeView to auto do saving aspect
class RestaurantLocationCreateForm(forms.ModelForm):
    # email = forms.EmailField(validators=[clean_email])
    # category = forms.CharField(required=False, validators=[validate_categories])
    class Meta:
        model = RestaurantLocation
        fields = [
                'name',
                'location',
                'category',
                ]

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == "Hello":
            raise forms.ValidationError("Not a valid name. Error rasied customlyfor 'Hello'")
        return name

    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     if "edu" in email:
    #         raise forms.ValidationError("We do not accept EDU emails")
    #     return email