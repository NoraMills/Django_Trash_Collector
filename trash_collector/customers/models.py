from django.db import models
# Create your models here.

# TODO: Finish customer model by adding necessary properties to fulfill user stories


class Customer(models.Model):
    PICKUP_DAYS = (
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday')
    )
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', blank=True,
                             null=True, on_delete=models.CASCADE)
    zip_code = models.CharField(max_length=5)
    reg_pickup = models.CharField(
        max_length=3, choices=PICKUP_DAYS, null=True, default='Mon')
    one_time_pickup = models.DateField(null=True, blank=True)
    suspension = models.BooleanField(default=False)
    sus_start = models.DateField(null=True, blank=True)
    sus_end = models.DateField(null=True, blank=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
