from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import time


@receiver(post_save, sender=User)
def user_created_signal(sender, instance, created, **kwargs):
    if created:
        print("Signal started...")
        time.sleep(5)  # Simulate a long-running task
        print(f"New user created: {instance.username}")
        print("Signal finished...")
