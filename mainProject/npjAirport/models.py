from django.db import models

# Create your models here.
class CSIT(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(max_length=20)

    class Meta:
        db_table = 'csit'

    def __str__(self) -> str:
        return self.name

