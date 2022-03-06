from django.db import models
from acc.models import User
# Create your models here.
class Board(models.Model):
    subject = models.CharField(max_length=200)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="writer")
    cotent = models.TextField()
    likey = models.ManyToManyField(User,blank = True,related_name="likey")
    pubdate = models.DateTimeField()
    
    def __str__(self):
        return self.subject
    
    def summary(self):
        if len(self.cotent) > 10:
            return f"{self.cotent[:200]} ..."
        return self.cotent
    
class Reply(models.Model):
    board = models.ForeignKey(Board,on_delete=models.CASCADE)
    replyer = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField()
    
    def __str__(self):
        return f"{self.board}_{self.replyer}"
    
