from django import forms

class FoodInputForm(forms.Form):
    type = forms.ChoiceField(choices=[("Starter", "starter"),("Main", "main"),("Dessert", "dessert"),("Drink","drink")])
    name = forms.CharField()
    stock = forms.IntegerField()
    price = forms.DecimalField()

class adminCheckForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password')
