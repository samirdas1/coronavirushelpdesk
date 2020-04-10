from django.db import models


class person_help(models.Model):
    name = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    contact = models.CharField(max_length=12)
    people = models.CharField(max_length=5, default=0)
    food = models.BooleanField(default=False, primary_key=False)
    sanitizer = models.BooleanField(default=False, primary_key=False)
    medical_supply = models.BooleanField(default=False, primary_key=False)

    def __str__(self):
        return self.name


class ngo_list(models.Model):
    ngo_name = models.CharField(max_length=50)
    ngo_district = models.CharField(max_length=30)
    ngo_state = models.CharField(max_length=30)
    contact = models.CharField(max_length=50, default=None, blank=True)

    def __str__(self):
        return self.ngo_state
