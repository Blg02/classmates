from django.db import models
from django.core.validators import RegexValidator

class Classmate(models.Model):
    name_validator = RegexValidator(
	regex=r'^[a-zA-Z]+$',
        message='Invalid Input:Only letters are allowed to the name.',
	)

    firstname = models.CharField(max_length=200, validators=[name_validator])
    lastname = models.CharField(max_length=200, validators=[name_validator])
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.firstname

    def get_absolute_url(self):
        return reverse('classmate_edit', kwargs={'pk': self.pk})

