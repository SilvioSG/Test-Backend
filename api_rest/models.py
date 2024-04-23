from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100, primary_key=True, default='')
    email = models.EmailField()
    password_hash = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"O seu nome é {self.name} e o seu email é {self.email}"
    

    def save(self, *args, **kwargs):
        if self.password_hash:
            self.password_hash = make_password(self.password_hash)
        super(User, self).save(*args, **kwargs)

    