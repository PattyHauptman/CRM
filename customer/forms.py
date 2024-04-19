from django import forms
from .models import Customer


class DateInput(forms.DateInput):
    input_type = "date"


class CustomerForm(forms.ModelForm):
    first_name = forms.CharField(
        label="Nome",
        error_messages={"max_length": "Máximo de 30 caracteres excedido."}
    )
    last_name = forms.CharField(
        label="Sobrenome",
        error_messages={"max_length": "Máximo de 30 caracteres excedido."}
    )
    birth_date = forms.DateField(label="Nascimento", widget=DateInput())
    email = forms.EmailField(label="E-mail")
    area_code = forms.RegexField(
        label="DDD",
        regex=r"^\+?1?[0-9]{2}$",
        error_messages={"invalid": "Número de DDD inválido"}
    )
    phone_number = forms.RegexField(
        label="Telefone",
        regex=r"^\d{8,9}$",
        error_messages={"invalid": "Número de Telefone inválido"}
    )
    address = forms.CharField(label="Endereço")
    neighborhood = forms.CharField(label="CPF")
    city = forms.CharField(label="Cidade")
    state = forms.CharField(label="Estado")

    class Meta:
        model = Customer
        fields = (
            "first_name",
            "last_name",
            "birth_date",
            "email",
            "area_code",
            "phone_number",
            "address",
            "neighborhood",
            "city",
            "state"
        )
