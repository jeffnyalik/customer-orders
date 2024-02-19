from django.db import models

class Customer(models.Model):
    name = models.CharField(blank=True, null=True, max_length=250)
    code = models.CharField(blank=True, null=True, max_length=50)

    def __str__(self) -> str:
        return f"{self.name} + {self.code}"
    

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    item = models.CharField(max_length=100, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True, blank=True, null=True)


    def __str__(self) -> str:
        return f"{self.customer} + {self.item}"
    