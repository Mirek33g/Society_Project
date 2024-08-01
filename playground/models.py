from django.db import models


class User(models.Model):
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    post_amount = models.SmallIntegerField(default=0)
    registered_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['last_name']


class Address(models.Model):
    address = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.address

    class Meta:
        ordering = ['address']


class Post(models.Model):
    POSITIVE = 'P'
    NEGATIVE = 'N'
    CHOICES = [
        (POSITIVE, 'Positive'),
        (NEGATIVE, 'Negative'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    post_type = models.CharField(max_length=1, choices=CHOICES, default=POSITIVE)
    placed_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['placed_at']
