from django.db import models
from django.urls import reverse
from django.utils.text import slugify
import uuid

# Create your models here.
class Lyric(models.Model):
    unique_num = models.UUIDField(default=uuid.uuid4, unique=True)
    title = models.CharField(max_length=144)
    song_writer = models.CharField(max_length=50)
    slug = models.SlugField(max_length=144)
    timestamp = models.SlugField(max_length=144)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('lyrics:complete', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        if not self.slug:
            slug_item = '{} {}'.format(self.title, self.unique_num)
            self.slug = slugify(slug_item)
        super().save(*args, **kwargs)


class Chorus(models.Model):
    lyric = models.ForeignKey(Lyric, on_delete=models.CASCADE)
    chorus = models.TextField(max_length=1024)

    def get_absolute_url(self):
        return reverse('lyrics:complete', args=[str(self.lyric.slug)])

    def __str__(self):
        return self.chorus


class Verse(models.Model):
    lyric = models.ForeignKey(Lyric, on_delete=models.CASCADE)
    verse = models.TextField(max_length=1024)

    def get_absolute_url(self):
        return reverse('lyrics:complete', args=[str(self.lyric.slug)])

    def __str__(self):
        return self.verse


class Bridge(models.Model):
    lyric = models.ForeignKey(Lyric, on_delete=models.CASCADE)
    bridge = models.TextField(max_length=1024)

    def get_absolute_url(self):
        return reverse('lyrics:complete', args=[str(self.lyric.slug)])
    
    def __str__(self):
        return self.bridge






