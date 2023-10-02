from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.


class Skill(models.Model):
    skill = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        indexes = [
            models.Index(fields=('skill',))
        ]
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.skill


class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    professional_summary = models.TextField(blank=True, null=False)
    skills = models.ManyToManyField(Skill)
    resume = models.FileField(upload_to='resume')
    linkedin_link = models.URLField(default='http://127.0.0.1:8000/', blank=True, null=False)
    github_link = models.URLField(default='http://127.0.0.1:8000/', blank=True, null=False)
    google_link = models.URLField(default='http://127.0.0.1:8000/', blank=True, null=False)

    class Meta:
        indexes = [
            models.Index(fields=('professional_summary',)),
            models.Index(fields=('resume',)),
            models.Index(fields=('linkedin_link', 'github_link', 'google_link')),
        ]
        verbose_name_plural = 'Portfolio'

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=50, blank=True, null=False)
    slug = models.SlugField(max_length=50, blank=True, null=False)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=('name',))
        ]
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:project_list_category', args=[self.slug])


class Project(models.Model):
    name = models.CharField(max_length=50, blank=True, null=False)
    slug = models.SlugField(max_length=50, blank=True, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='project_categories')
    project_img = models.ImageField(upload_to='projects_img', blank=True, null=True)
    website_url_on = models.BooleanField(default=False)
    website_url = models.URLField(default='http://127.0.0.1:8000/', blank=True, null=False)
    git_url_on = models.BooleanField(default=False)
    git_url = models.URLField(default='http://127.0.0.1:8000/', blank=True, null=False)
    video_link_on = models.BooleanField(default=False)
    video_link = models.URLField(default='http://127.0.0.1:8000/', blank=True, null=False)
    description = models.TextField(blank=True, null=True)
    done = models.BooleanField(default=False)
    date_done = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=('name',))
        ]
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:project_detail', args=[self.slug])


class Contact(models.Model):
    name = models.CharField(max_length=100, null=True, verbose_name='Your Name')
    email = models.EmailField(null=True, verbose_name='Your Email')
    subject = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=('name',))
        ]
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.name
