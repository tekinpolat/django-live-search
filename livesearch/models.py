from django.db import models

class Person(models.Model):
    id      = models.AutoField(primary_key=True)
    name    = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    
    class Meta:
        db_table = 'persons'
