from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager

GENDER = (
    ('M', 'M'),
    ('F', 'F'),
)

PROFILE = (
    ('Consommateur', 'Consommateur'),
    ('Partenaire', 'Partenaire'),
    ('Ambassadeur', 'Ambassadeur'),
)

class CustomUser(AbstractUser):
    full_name = models.CharField(('full_name'), max_length=50)
    email = models.EmailField(('email'), unique=True)
    phone = models.CharField(('phone'), max_length=15)
    birthday = models.DateField(('birthday'),)
    gender = models.CharField(('gender'), choices=GENDER, max_length=1)
    profile = models.CharField(('profile'), choices=PROFILE, max_length=15)

    objects = UserManager()

    def __str__(self):
        return f'{self.username}'
