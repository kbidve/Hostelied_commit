from django.db import models

class UserInfo(models.Model):
    name = models.CharField(max_length=200 , default="some string")
    contact_no = models.CharField(max_length=10, default="some string")
    email_id = models.EmailField()
    password = models.CharField(max_length=100 , default="some string")
    
    def __str__(self):
        return self.name