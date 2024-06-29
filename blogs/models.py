# blog/models.py
from django.db import models
from django.contrib.auth.models import User, Permission, Group
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType

STATUS_CHOICES = [
    ('draft', 'Draft'),
    ('pending', 'Pending'),
    ('published', 'Published'),
    ('rejected', 'Rejected'),
]

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    tags = models.ManyToManyField(Tag)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def admin_labels(self):
        return AdminLabel.objects.filter(blog_post=self)


class AdminLabel(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    label = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.blog_post.title} - {self.label}"

class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

class Like(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} likes {self.post}"


@receiver(post_migrate)
def create_permissions(sender, **kwargs):
    content_type = ContentType.objects.get_for_model(BlogPost)
    add_label_perm, created = Permission.objects.get_or_create(
        codename='add_adminlabel',
        name='Can add admin label',
        content_type=content_type
    )
    remove_label_perm, created = Permission.objects.get_or_create(
        codename='remove_adminlabel',
        name='Can remove admin label',
        content_type=content_type
    )
    
    admin_group, created = Group.objects.get_or_create(name='admin')
    if created:
        admin_group.permissions.add(add_label_perm, remove_label_perm)