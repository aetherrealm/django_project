from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class IP_Addresses(models.Model):
    IP = models.GenericIPAddressField()
    def __str__(self):
        return self.IP

class VLANs(models.Model):
    VID = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(4093)])
    def __str__(self):
        return str(self.VID)