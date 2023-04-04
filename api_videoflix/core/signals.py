from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Video
from core.tasks import convert, convert_360p
import django_rq
from .utils import deleteVideoFiles


@receiver(post_save, sender=Video)
def video_post_save(sender, instance, created, **kwargs):
    if created:
        queue = django_rq.get_queue("default", autocommit=True)
        queue.enqueue(convert_360p, instance.video_file.path)
        queue.enqueue(convert, instance.video_file.path, 480)
        queue.enqueue(convert, instance.video_file.path, 720)
        queue.enqueue(convert, instance.video_file.path, 1080)


@receiver(post_delete, sender=Video)
def video_post_delete(sender, instance, using, **kwargs):
    deleteVideoFiles(instance.video_file)


# if instance.video_file:
#     if os.path.isfile(instance.video_file.path):
#         os.remove(instance.video_file.path)
