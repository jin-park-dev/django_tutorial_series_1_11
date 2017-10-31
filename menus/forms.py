from django import forms

from restaurants.models import RestaurantLocation

from .models import Item



class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
                'restaurant',
                'name',
                'contents',
                'excludes',
                'public'
                ]
    # def __init__(self,*args, **kwargs):
    #     print(kwargs.pop('user'))
    #     super(ItemForm, self).__init__(*args, **kwargs)

    def __init__(self, user=None, *args, **kwargs):
        print(user)
        print(kwargs)
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['restaurant'].queryset = RestaurantLocation.objects.filter(owner=user)
        #.exclude(item__isnull=False) if relationhsip is null. So empty item is not showing

        # RestaurantLocation.objects.filter(owner=user, item__isnull=False)