from django.db import models
from django.contrib.auth.models import User

class Register(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.IntegerField()
    address = models.TextField(null=True)
    pin_code = models.PositiveIntegerField()
    gov_id = models.ImageField(upload_to="gov_ids", null=True)
    is_volunteer = models.BooleanField(default = False)

    def __str__(self):
        return str(self.user)
