from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Post, User


@receiver(post_save, sender=Post)
def update_post_amount_on_save(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        user.post_amount = Post.objects.filter(user=user).count()
        user.save()


@receiver(post_delete, sender=Post)
def update_post_amount_on_delete(sender, instance, **kwargs):
    user = instance.user
    user.post_amount = Post.objects.filter(user=user).count()
    user.save()
