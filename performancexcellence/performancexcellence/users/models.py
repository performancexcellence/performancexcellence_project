from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile_user', null=True, blank=True)
    is_athlete = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='static/profiles/', default="profiles/profile_default.png")
    birth_date = models.DateField(null=True, blank=True)
    gender_choices = (('M', 'Masculino'), ('F', 'Feminino'))
    gender = models.CharField(max_length=10, choices=gender_choices)
    birth_place = models.CharField(max_length=200, blank=True, null=True)
    nationality = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.user.username)
    

    @property
    def imageURL(self):
        try:
            url = self.profile_image.url
            # Remove o prefixo 'static/' da URL
            if url.startswith('static/'):
                url = url[len('static/'):]
        except:
            url = ''
        return url
