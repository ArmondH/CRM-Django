from django.db import models
from django.db.models.enums import Choices
from django.contrib.auth.models import AbstractUser

# CREATING A USER MODEL


class User(AbstractUser):
    pass


# CREATED A DATABASE TABLE CALLED LEADS WITH AGENT AS A FOREIGNKEY: FIRSTNAME /LASTNAME STRING FELIDS
class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    # ALLOWS LEADS TO CREATE A RELATIONSHIP WITH OTHER MODEL AGENT & EVERY LEAD HAS A AGENT &DELETE AGENT
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)
    # SHOWING THE NAME IN THE ADMIN PAGE IN A STRING

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email
