from email.policy import default
from itertools import count
from unicodedata import category
from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils.text import slugify
from django.core.mail import send_mail
from portfolio.settings import EMAIL_HOST_USER
from embed_video.fields import EmbedVideoField
from cloudinary_storage.storage import VideoMediaCloudinaryStorage
from cloudinary_storage.validators import validate_video


# These models are form home page
class HomepageProfile(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    position = models.CharField(max_length=100, verbose_name='Position')
    description1 = RichTextField(verbose_name='Description')
    description2 = RichTextField(verbose_name='Description')
    description3 = RichTextField(verbose_name='Description',blank = True, null = True)
    description4 = RichTextField(verbose_name='Description',blank = True, null = True)
    resume_url = models.URLField(verbose_name='Resume URL')
    image1 = models.ImageField(upload_to='profile/', blank=True,default='')
    image2 = models.ImageField(upload_to='profile/', blank=True,default='')
    video_url = EmbedVideoField(verbose_name='Video URL', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ServicesSlider(models.Model):
    icon = models.CharField(max_length=100,default='fa fa-cogs')
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    review = models.TextField()
    client_image = models.ImageField(upload_to='profiles/',blank = True,default='')
    client_name = models.CharField(max_length=255)
    client_place = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.client_name

class Achievements(models.Model):
    icon  = models.CharField(max_length=100,default='fa fa-cogs')
    title = models.CharField(max_length=255)
    count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# These models for blog page
class Blog(models.Model):

    category_choices = (
        ('Python', 'Python'),
        ('Stats', 'Stats'),
        ('Machine Learning', 'Machine Learning'),
        ('Deep Learning', 'Deep Learning'),
        ('NLP', 'NLP'),

    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    snippet = models.CharField(max_length=255)
    description = RichTextField()
    image = models.ImageField(upload_to='blogs/', blank=True,default='')
    category = models.CharField(choices=category_choices,max_length=255)
    author = models.CharField(max_length=255)
    time_to_read = models.CharField(max_length=255)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})


class Project(models.Model):

    category_choices = (
        ('Python', 'Python'),
        ('Stats', 'Stats'),
        ('Machine Learning', 'Machine Learning'),
        ('Deep Learning', 'Deep Learning'),
        ('NLP', 'NLP'),

    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    snippet = models.CharField(max_length=255)
    description = RichTextField()
    image = models.ImageField(upload_to='projects/',blank = True,default='')
    category = models.CharField(choices=category_choices,max_length=255)
    author = models.CharField(max_length=255)
    time_to_read = models.CharField(max_length=255)
    git_url = models.CharField(max_length=255)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug': self.slug})


# models for my work page

class Repositary(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField()
    git_url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# These models are from contact page
class Adress(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # send an email to the user



    def __str__(self):
        return self.name + ' ' + self.email


# These models are from about page

class Subscribers(models.Model):
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

class Mailmessage(models.Model):
    subject = models.CharField(max_length=255,null=True)
    message = models.TextField(null=True)
    users = models.ManyToManyField(Subscribers)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    send_it = models.BooleanField(default=False)

    def __str__(self):
        return self.subject

    # how to save all the fields in the database
    def save(self, *args, **kwargs):
        super(Mailmessage, self).save(*args, **kwargs)
        if self.send_it:
            for user in self.users.all():
                send_mail(self.subject,
                    self.message,
                    EMAIL_HOST_USER,
                    [user.email]
                )
            self.send_it = False
            self.save()

    

    
    class Meta:
        verbose_name_plural = "Emails to send"
        verbose_name = "Emails to send"
        

class AboutProfile(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255,null=True)
    image = models.ImageField(upload_to='profile/',blank = True,default='')
    text1 = models.TextField(null=True)
    description1 = RichTextField()
    text2 = models.TextField(null=True)
    description2 = RichTextField()
    text3 = models.TextField(null=True)
    description3 = RichTextField()
    age = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    Place = models.CharField(max_length=255)
    resume_url = models.CharField(max_length=255)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Socialmedia(models.Model):
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    socialmediaurl = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class AboutServices(models.Model):
    name = models.CharField(max_length=255)
    icons = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Aboutskills(models.Model):
    name = models.CharField(max_length=255)
    percent = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class AboutPersonalAwards(models.Model):
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    



    
