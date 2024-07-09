from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Room(models.Model):
    name=models.CharField(max_length=225)
    slug=models.SlugField(unique=True) # A slug is a short, human-readable, and unique identifier for a web page or resource. It's typically used in the URL of a web page to make it more user-friendly and SEO-friendly. For example, in a blog post URL like "https://example.com/blog/my-awesome-post/", the slug would be "my-awesome-post"
    
    def __str__(self):
        return self.name
    # The __str__method in Django models is used to provide a human-readable string representation of the model instance. It is a special method in Python that is called when you try to convert an object to a string, such as when printing the object or using it in a template.
    # For example, if you have a `Transaction` model, the `__str__` method can be used to display the transaction details in a more user-friendly way, such as `"John Doe - Groceries - Bought milk"` instead of the default string representation, which might be something like `"<Transaction object (1)>"`.
    
class ChatMessage(models.Model):
    room =models.ForeignKey(Room,related_name='messages',on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('date_added',) # This line specifies that the messages should be ordered by the date they were added in ascending order. The `ordering` attribute is a special attribute in Django models that allows you to specify the order in which the model instances should be retrieved or displayed. In this case, we're ordering the messages by the `date_added` field in ascending order.

    def __str__(self):
        return f"{self.user.username} - {self.room.name}"