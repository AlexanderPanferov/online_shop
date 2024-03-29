from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class CatalogForms(StyleFormMixin, forms.ModelForm):
    error_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар', ]

    class Meta:
        model = Product
        exclude = ('owner', 'is_active')

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        if cleaned_data in self.error_list:
            raise forms.ValidationError('Запрещенное название')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        if cleaned_data in self.error_list:
            raise forms.ValidationError('Запрещенное описание')

        return cleaned_data


class ModeratorForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('description', 'category', 'is_active')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields["is_active"].widget.attrs['class'] = 'form-check-input'


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
