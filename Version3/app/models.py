from django.db import models
from django.contrib.auth.models import User, UserManager

# Create your models here.
class Profile(User):
    avatar = models.ImageField(upload_to='avatars', default='avatars/user.png')
    objects = UserManager()

class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Question_manager(models.Manager):
    def last_questions(self):
        return self.order_by('-created_at')

    def hot_questions(self):
        return self.order_by('-rating')

class Question(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    correct_answer = models.OneToOneField('Answer', related_name='+', null=True, blank=True,on_delete=models.CASCADE)
    objects = Question_manager()

    def __str__(self):
        return '{}; user: {}; updated_at: {}'.format(self.title, self.user, self.updated_at)


class Answer_manager(models.Manager):
    def last_answers(self):
        return self.order_by('-created_at')


class Answer(models.Model):
    text = models.TextField()
    rating = models.IntegerField(default=0)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Answer_manager()

    def __str__(self):
        return '{}; updated_at: {}; {}'.format(self.user, self.updated_at, self.text)


class QuestionLike(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_like = models.BooleanField()


class AnswerLike(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    is_like = models.BooleanField()
