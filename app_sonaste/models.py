from django.db import models

class User(models.Model):
    class Meta:
         db_table = 'user_table'

    user  =  models.CharField(max_length=200)
    password  =  models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

def __str__(self):
    return f"El nombre es : {self.user}, su correo es {self.email}"

def get_fields(self):
    return [
        (field.verbose_name, field.value_from_object(self))
        for field in self.__class__._meta.fields[1:]
    ]