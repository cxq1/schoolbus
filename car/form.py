from django import forms

class PathForm(forms.Form):
    path = forms.CharField()

class QueryShfitForm(forms.Form):
    fromStation=forms.CharField()
    train_start_date=forms.DateField()
    car_type=forms.CharField()

class OrderForm(forms.Form):
    shitf_id = forms.IntegerField()
    car_num=forms.CharField()
    path = forms.CharField()
    times = forms.DateField()
    price =forms.FloatField()