from django.db import models

class Uzum(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.IntegerField()
    count = models.IntegerField()
    image = models.ImageField(upload_to="images/")
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


class Order(models.Model):
    user_name = models.CharField(max_length=100)
    product = models.ForeignKey(Uzum, on_delete=models.CASCADE)
    # count = models.IntegerField()
    # total_price = models.IntegerField()
    adress = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} - {self.product.name}"