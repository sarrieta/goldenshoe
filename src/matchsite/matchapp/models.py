from django.contrib.auth.models import User
from django.db import models

"""
	Profile image,	
    email,	
    gender,	
    date of	birth, 
    and	a list	of	hobbies.
"""
class Profile(models.Model):
    image = models.ImageField(upload_to='profile_images')
    email = models.EmailField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dob = models.DateField(max_length=8)
    # List of hobbies in text form or na?
    text = models.CharField(max_length=4096)

    # True if this profile belongs to a Member
    @property
    def has_member(self):
        return hasattr(self, 'member') and self.member is not None

    # Either the username of the Member, or NONE
    @property
    def member_check(self):
        return str(self.member) if self.has_member else 'NONE'

    def __str__(self):
        return self.text + ' (' + self.member_check + ')'

# Django's User model already has username and password
# both of which are required fields, so Member inherits
# these fields

class Member(User):
    profile = models.OneToOneField(
        to=Profile,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    hobbies = models.ManyToManyField(
        to='self',
        blank=True,
        symmetrical=False,
        through='Hobby',
        related_name='related_to'
    )

    # one property that counts hobbies for member
    @property
    def hobbies_count(self):
        return self.hobbies.count()

    def __str__(self):
        return self.username

# The Hobby models provides an intermediate model for
# the 'hobbies' ManyToMany relationship between Members
# Pre-defined hobbies to be entered into the database

class Hobby(models.Model):
    user = models.ForeignKey(
        to=Member,
        related_name='hobbies',
        on_delete=models.CASCADE
    )

    # Given hobby
    # Tennis, basketball, running, gym etc
    hobby = models.CharField(max_length=4096)

    def __str__(self):
        return self.user.username       

