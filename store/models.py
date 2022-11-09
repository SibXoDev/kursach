from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

def directory_path(instance, filename):
    # if instance.file_name:
    #     filename = f'{instance.file_name}.{filename.split(".")[-1]}'
    return "uploads/{0}/{1}".format(instance.folder_name, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    games = models.ManyToManyField("Game", related_name="games", blank=True)
    favorites = models.ManyToManyField("Game", related_name="favorites", blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if "Profile" in instance._meta.get_fields():
        instance.profile.save()

class Game(models.Model):
    name = models.CharField(max_length = 255, default = None)
    price = models.IntegerField(default = 0)
    preview = models.ImageField(upload_to = "uploads/preview/", default = None)
    description = models.TextField(null=True, blank=True)
    release_date = models.DateField(default = datetime.date.today)
    sys_req = models.OneToOneField("SystemRequirements", on_delete = models.CASCADE)
    tags = models.ManyToManyField("Tag", blank=True)
    media = models.ManyToManyField("Media", blank=True)
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length = 255, default = None)

    def __str__(self):
        return self.name

class Media(models.Model):
    folder_name = models.CharField(max_length = 255, default = None)
    file = models.FileField(upload_to = directory_path, default = None)

    def __str__(self):
        return f'{self.folder_name}/{self.file.name.split("/")[-1]}'

class SystemRequirements(models.Model):
    os = models.CharField(max_length = 128, default = None)
    cpu = models.CharField(max_length = 128, default = None)
    ram = models.IntegerField(default = 0)
    gpu = models.CharField(max_length = 128, default = None, null=True, blank=True)
    disk_space = models.IntegerField(default = 0)

    # def __str__(self):
    #     return self.game.name