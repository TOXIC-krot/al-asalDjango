from django.db import models


class Cart(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    item = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item} - {self.quantity} pcs"
