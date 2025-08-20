from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=100)
    image = models.ImageField(upload_to="blog-images")
    sub_title=models.CharField(max_length=500)
    short_description=models.TextField(max_length=500)
    description=models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        db_table ="blogs"

class Comments(models.Model):
    review=models.CharField(max_length=200)
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)

    class Meta:
        db_table="comment"

        