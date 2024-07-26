from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    registered_at = models.DateField()


class Address(models.Model):
    address = models.TextField()
    user_address = models.ForeignKey(User, on_delete=models.CASCADE)


class Posts(models.Model):
    POSITIVE = 'P'
    NEGATIVE = 'N'
    CHOICES = [
        (POSITIVE, 'Positive'),
        (NEGATIVE, 'Negative'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    post_type = models.CharField(max_length=1, choices=CHOICES, default=POSITIVE)
    placed_at = models.DateTimeField()
    user_post = models.ForeignKey(User, on_delete=models.PROTECT)
