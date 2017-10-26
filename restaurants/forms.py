from django import forms

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