from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.name


class Agency(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    image = models.ImageField()
    cats = models.ManyToManyField(Category)
    description = models.TextField()
    rates = models.IntegerField()
    location = models.CharField(max_length=255)
    year = models.IntegerField()
    employees = models.CharField(max_length=255)
    services = models.TextField()
    scores = models.CharField(max_length=255, default='5')

    def __str__(self):
        return self.name


class Review(models.Model):
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    review = models.TextField()
    score = models.TextField(max_length=255)

    def __str__(self):
        return self.name
