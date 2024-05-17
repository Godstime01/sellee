from django import forms
from .models import Card, Coin


class CardCreationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = (
                "border border-gray-300 text-white bg-transparent sm:text-sm rounded-sm focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"
            )

    class Meta:
        model = Card
        fields = ["name", "type", "currency", "image"]


class CoinCreationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = (
                "border border-gray-300 text-white bg-transparent sm:text-sm rounded-sm focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5"
            )

    class Meta:
        model = Coin
        fields = "__all__"
