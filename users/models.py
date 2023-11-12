from django.db import models
from django.contrib.auth.models import AbstractUser



class School(models.Model):
    school_name = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.school_name


class Grade(models.Model):
    student_grade = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.student_grade


class SignupUser(AbstractUser):
    school_email = models.EmailField(null=True, blank=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='signup_school', null=True, blank=True)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='signup_grade', null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    confirm_password = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)



# Create your models here.
