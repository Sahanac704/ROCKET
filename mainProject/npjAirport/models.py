from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Base(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, db_column="created_by", null = True, related_name = "+")
    created_at = models.DateTimeField(null = True)

    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, db_column="updated_by", null=True, related_name="+")
    updated_at = models.DateTimeField(null=True)

    is_delete = models.BooleanField(default=False)

    class Meta:
        abstract = True


class CSIT(Base):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(max_length=20)

    class Meta:
        db_table = 'csit'

    def __str__(self) -> str:
        return self.name

