from django.db import models
from django.contrib.auth.models import User
from movies.models import Title

# обзор

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    text = models.TextField()
    raiting = models.CharField(max_length=50,choices=[
    ('0','0'),
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7'),
    ('8','8'),
    ('9','9'),
    ('10','10'),
    ], default='0',) # выборка рейтинга

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# комментарии на обзоры

class ReviewComment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments') # обзор под которым оставлен комментарий
    user = models.ForeignKey(User, on_delete=models.CASCADE) # кем был оставлен комментарий
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # когда был создан комментарий 

# лайки на обзоры

class ReviewLike(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='likes') # обзор
    user = models.ForeignKey(User, on_delete=models.CASCADE) # кто поставил лайк
    created_at = models.DateTimeField(auto_now_add=True) # когда поставили лайк



















