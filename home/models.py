from django.db import models
import uuid
from django.contrib.auth.models import User


# Create your models here.
# class BaseModel(models.Model):
#     uid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     class Meta:
#         abstract = True



# class Colors(BaseModel):
#     Color_code = models.CharField(max_length=100)


# class People(BaseModel):
#     name = models.CharField(max_length=100)
#     about = models.TextField()
#     age = models.IntegerField()
#     email = models.EmailField()
#     colors = models.ManyToManyField(Colors)


# class PeopleAddress(BaseModel):
#     people = models.ForeignKey(People, on_delete=models.CASCADE, related_name="address")
#     address_field = models.TextField()




# class Fruits(models.Model):
#     fruit_name = models.CharField(max_length=100, null=True, blank=True)
#     price = models.IntegerField()
#     manufacture_date = models.DateField()
#     fruits_description = models.TextField()
#     is_fresh = models.BooleanField(default=True)


#     def __str__(self):
#         return self.fruit_name


#     class Meta:
#         db_table = 'home_fruits'
#         ordering = ['fruit_name']
#         unique_together = [['fruit_name', 'price']]