from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.gis.db import models as gismodels
from django.contrib.gis.geos import Point
from datetime import *
from django.contrib.auth.models import User

def return_date_time():
    now = datetime.now()
    return now + timedelta(days=10)


class JobType(models.TextChoices):
    Permanent = "Permanent"
    Temporary = 'Temporary'
    Internship = 'Internship'


class Education(models.TextChoices):
    Bachelors = "Bachelors"
    Masters = "Masters"
    Phd = "Phd"


class Industry(models.TextChoices):
    Business = "Business"
    IT = "Information Technology"
    Banking = "Banking"
    Education = "Education/Training"
    Telecommunication = "Telecommunication"
    Other = "Other"


class Experience(models.TextChoices):
    NO_EXPERIENCE = "No Experience"
    ONE_YEAR = "1 year"
    TWO_YEAR = "2 years"
    THREE_YEARS_PLUS = "3 years above"


class Job(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    email = models.EmailField(null=True)
    adress = models.CharField(max_length=200, null=True)
    jobType = models.CharField(
        max_length=50,
        choices=JobType.choices,
        default=JobType.Permanent
    )
    education = models.CharField(
        max_length=50,
        choices=Education.choices,
        default=Education.Bachelors
    )
    industry = models.CharField(
        max_length=50,
        choices=Industry.choices,
        default=Industry.Business
    )
    experience = models.CharField(
        max_length=50,
        choices=Experience.choices,
        default=Experience.NO_EXPERIENCE
    )
    salary = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    positions = models.IntegerField(default=1)
    company = models.CharField(max_length=100, null=True)
    point = gismodels.PointField(default=Point(0.0,0.0))
    lastDate = models.DateTimeField(default=return_date_time)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
