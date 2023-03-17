from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Video
from core.tasks import convert_480p
import django_rq

# import os


@receiver(post_save, sender=Video)
def video_post_save(sender, instance, created, **kwargs):
    print("Video wurde gespeichert")
    if created:
        print("New video created")
        queue = django_rq.get_queue("default", autocommit=True)
        queue.enqueue(convert_480p, instance.video_file.path)
        # convert_480p(instance.video_file.path)


@receiver(post_delete, sender=Video)
def video_post_delete(sender, instance, using, **kwargs):

    # name = instance.video_file.name
    try:
        instance.video_file.delete(save=False)
        print("Video wurde gelöscht")
    except:
        pass

    # if instance.video_file:
    #     if os.path.isfile(instance.video_file.path):
    #         os.remove(instance.video_file.path)
