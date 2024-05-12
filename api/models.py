from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.name



class memberProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = "Member_Profile")
    
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    photo = models.FileField(null=True, blank=True, upload_to='member_photo')
    age = models.IntegerField(null=False)
    gender = models.CharField(choices=(('M', 'Male'), ('F', 'Female'), ('O', 'Other')), max_length=10, null=True, blank=True)
    
    playing_in = models.ManyToManyField(to=category,)
    contact_number = models.CharField(max_length=15)
    email_id = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(max_length=300, null=True, blank=True)
    school_college = models.TextField(max_length=200, null=True, blank=True)
    # gender = models.CharField(max_length=10)
    # is_admin = models.BooleanField(default=False)
    approved = models.BooleanField(default=False, null=True, blank=True)
    paid_registration_fee = models.BooleanField(default=False, null=True, blank=True)
    paid_this_month_fee = models.BooleanField(default=False, null=True, blank=True)
    fee_pending = models.IntegerField(default = 0, null=True, blank=True,)

    achievements = models.TextField(null=True, blank=True, max_length=1000)
    comments = models.TextField(max_length=1000,null=True, blank=True)

    def __str__(self) -> str:
        return self.user.username
    # category = models.on

class newsAndHighlight(models.Model):
    title = models.TextField(max_length=200)
    details = models.TextField(max_length=1000, null=True, blank=True)
    links = models.CharField(max_length=200, null=True, blank=True)
    image = models.FileField(null=True, blank=True, upload_to='news_photo')
    date = models.DateField(null=True, blank=True)
    def __str__(self) -> str:
        return str(self.date) + self.title[:10]

class contactMsg(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    message = models.TextField(max_length=1000)
    reply_pending = models.BooleanField(default=True)
    def __str__(self) -> str:
        return self.name