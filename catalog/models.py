from django.db import models
from slugify import slugify


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, blank=True, unique=True)
    description = models.CharField(max_length=255, blank=True)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Categories"


class Agency(models.Model):
    name = models.CharField(max_length=255)
    # new
    logo = models.ImageField(upload_to='logos', blank=True)
    website = models.URLField(blank=True)
    slug = models.CharField(max_length=255, unique=True)
    origin_image = models.URLField(blank=True)
    cats = models.ManyToManyField(Category)
    #new have no parser func
    short_description = models.TextField(blank=True)
    description = models.TextField(blank=True)
    rates = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    year = models.IntegerField(blank=True)
    employees = models.CharField(max_length=255, blank=True)
    services = models.TextField(blank=True)
    scores = models.CharField(max_length=255, default='5')
    email = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    address = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Agencies"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Review(models.Model):
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=255)
    summary = models.CharField(max_length=255, blank=True)
    review = models.TextField(blank=True)
    score = models.TextField(max_length=255, default='5', blank=True)

    def __str__(self):
        return self.name
