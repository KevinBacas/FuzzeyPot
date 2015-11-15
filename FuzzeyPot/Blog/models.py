from django.db import models

# Create your models here.
class BlogPost(models.Model):
    """Represents a Blog post with a text and a publication date"""
    post_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.post_text
