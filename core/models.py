from django.db import models

class IP_Addresses(models.Model):
    IP = models.GenericIPAddressField(protocol="IPv4")
    def __str__(self):
        return self.IP
