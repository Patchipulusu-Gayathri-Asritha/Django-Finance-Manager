from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

#Create your models here.

SELECT_CATEGORY_CHOICES = [
    ("Food", "Food"),
    ("Travel", "Travel"),
    ("Shopping", "Shopping"),
    ("Necessities", "Necessities"),
    ("Entertainment", "Entertainment"),
    ("Other", "Other")
]

ADD_EXPENSE_CHOICES = [
    ("Expense", "Expense"),
    ("Income", "Income")
]

PROFESSION_CHOICES = [
    ("Employee", "Employee"),
    ("Business", "Business"),
    ("Student", "Student"),
    ("Other", "Other")
]

class Addmoney_info(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    add_money = models.CharField(max_length=10, choices=ADD_EXPENSE_CHOICES)
    quantity = models.BigIntegerField()
    Date = models.DateField(default=now)
    Category = models.CharField(max_length=20, choices=SELECT_CATEGORY_CHOICES, default='Food')

    def __str__(self):
        return f"{self.user.username} - {self.add_money} - ₹{self.quantity}"

    class Meta:
        db_table = 'addmoney'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profession = models.CharField(max_length=10, choices=PROFESSION_CHOICES, null=True, blank=True)
    Savings = models.IntegerField(null=True, blank=True)
    income = models.BigIntegerField(null=True, blank=True)
    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)

    def __str__(self):
        return self.user.username
