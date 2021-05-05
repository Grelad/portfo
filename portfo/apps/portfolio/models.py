from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Portfolio(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} | {self.owner}.'

    @staticmethod
    def get_absolute_url():
        return reverse('portfolio:portfolio')

    def get_portfolio_images(self):
        return Image.objects.filter(portfolio__pk=self.id)


class Image(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    photo = models.ImageField(upload_to='uploaded_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_parent_portfolio(self):
        return reverse('portfolio:portfolio_details', args=self.portfolio_id)


class Comment(models.Model):
    image = models.ForeignKey(Image, related_name='comments', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField(max_length=1000)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.image.name, self.user)
