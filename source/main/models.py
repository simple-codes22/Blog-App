from django.db import models
from django.utils import timezone

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    e_mail = models.EmailField(editable=True)
    username = models.CharField(max_length=30, default="Anonymous")
    is_publisher = False
    def get_name(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"<user>Name: {self.first_name} {self.last_name}, ID: {self.id}</user>"

class Publisher(User):
    password = models.CharField(unique=True, null=False, blank=False, max_length=50)
    is_publisher = True

    def __repr__(self):
        return f"<publisher> {self.first_name} {self.last_name}, ID: {self.id}</publisher>"

class Post(models.Model):
    title = models.CharField(blank=False, null=False, max_length=100, editable=True)
    post = models.TextField(blank=False, null=False, editable=True)
    date_posted = models.DateField(auto_created=True, default=timezone.now, editable=False)
    author = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __repr__(self):
        return f"""<Post> Title: {self.title}, Author: {self.author.get_name()}</Post>"""


# Create your models here.
