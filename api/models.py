from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    price = models.PositiveBigIntegerField(null=False, default=0)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_date = models.DateField()
    updated_date = models.DateField()

    def __str__(self):
        return self.name