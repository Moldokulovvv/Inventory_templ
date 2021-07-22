from django.db import models

from django.db import models


class Oblast(models.Model):
    slug = models.SlugField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name




class Address(models.Model):
    slug = models.SlugField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
    oblast = models.ForeignKey(Oblast, on_delete=models.CASCADE, related_name='oblasts')
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        if self.parent:
            return f'{self.parent} --> {self.name}'
        return self.name


class Institution(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='institution', blank=True, null=True)
    oblast = models.ForeignKey(Oblast, on_delete=models.CASCADE, related_name='oblasti')
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='institutions')

    def __str__(self):
        return self.name
