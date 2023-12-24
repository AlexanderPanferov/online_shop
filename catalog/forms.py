from django import forms

from catalog.models import Product


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class CatalogForms(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        error_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар', ]
        if cleaned_data in error_list:
            raise forms.ValidationError('Запрещенное название')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        error_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар', ]
        if cleaned_data in error_list:
            raise forms.ValidationError('Запрещенное описание')

        return cleaned_data
