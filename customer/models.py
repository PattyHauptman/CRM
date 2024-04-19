from django.db import models
from django.urls import reverse

# Create your models here.
# Classes são a representação de um objeto no banco de dados. Criar tabela, utilizando objetos Python e django.


class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    email = models.EmailField()
    area_code = models.CharField(max_length=3)
    phone_number = models.CharField(max_length=9)
    address = models.CharField(max_length=50)
    neighborhood = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def _str_(self):
        return f"{self.first_name} {self.last_name}"

    def get_full_phone_number(self):
        return f"({self.area_code}) {self.phone_number}"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_full_city(self):
        return f"{self.city} - {self.state}"

    def get_absolute_url(self):
        return reverse("customer:customer-update", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("customer:customer-delete", kwargs={"id": self.id})
    class Meta:
        db_table = "customer"
