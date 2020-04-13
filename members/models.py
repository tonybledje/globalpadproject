from django.db import models
from django.utils import timezone

# Create your models here.


class Chapter(models.Model):
    code_chapter = models.CharField(max_length=3)
    chapter_name = models.CharField(max_length=150)

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.chapter_name)


class Member(models.Model):
    MARRIED = 'M'
    WIDOWED = 'W'
    SINGLE = 'S'

    Marital_Status = [
        (MARRIED, 'Married'),
        (WIDOWED, 'Widowed'),
        (SINGLE, 'Single'),
    ]

    memberFName = models.CharField(max_length=35)
    memberMidInitial = models.CharField(max_length=1)
    memberLName = models.CharField(max_length=35)
    memberAdmissionDate = models.DateField('Admitted on:')
    memberGender = models.CharField(max_length=1, blank=False)
    MemberMaritalStatus = models.CharField(max_length=2, choices=Marital_Status, default=MARRIED)
    memberInPadSocial = models.BooleanField()
    dateAdmitted = models.DateField()
    MemberCellPhone = models.CharField(max_length=12)
    memberHomePhone = models.CharField(max_length=12)
    memberAddress = models.TextField()
    memberCity = models.CharField(max_length=100)
    memberState = models.CharField(max_length=100)
    memberZip = models.CharField(max_length=6)

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.memberLName)


