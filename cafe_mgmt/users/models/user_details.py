from django.core.validators import (MinLengthValidator, MaxLengthValidator)
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserDetails(models.Model):

    class StautsType(models.IntegerChoices):
        DISABLE = 0, _("Disable")
        ENABLE = 1, _("Enable")
        DELETED = 2, _("Deleted")

    first_name = models.CharField(max_length=512, 
        validators=[MinLengthValidator(3)])
    last_name = models.CharField(null=True, blank=True, max_length=512,
        validators=[MinLengthValidator(3)])
    mob_number = models.CharField(unique=True,
        validators=[MinLengthValidator(10), MaxLengthValidator(10)])
    email = models.EmailField(unique=True, max_length=512)
    password = models.CharField(max_length=512, 
        validators=[MinLengthValidator(4), MaxLengthValidator(50)])
    status = models.IntegerField(choices=StautsType.choices, default=StautsType.DISABLE)
    activation_slug = models.CharField(null=True, blank=True, max_length=500)

    
    def __str__(self):
        return self.email
    

    def get_full_name(self):
        full_name = f'{self.first_name}'
        if self.last_name:
            full_name += f' {self.last_name}'
        full_name = full_name.strip().title()
        return full_name


    class Meta:
        ordering = ['-id']