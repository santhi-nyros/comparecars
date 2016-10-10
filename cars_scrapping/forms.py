from django import forms

class SearchingForm(forms.Form):   

    search_word =  forms.CharField(max_length=200)