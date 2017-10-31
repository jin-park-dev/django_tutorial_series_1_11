from django import forms

from .models import RestaurantLocation
from .validators import validate_categories

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
    class Meta:
        model = RestaurantLocation
        fields = [
                'name',
                'location',
                'category',
                'slug'
                ]

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == "Hello":
            raise forms.ValidationError("Not a valid name. Error rasied customlyfor 'Hello'")
        return name