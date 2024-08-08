from django import forms


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "quantity-input", "placeholder": 0})
    )
    update = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput
    )  # Update part is not needed
