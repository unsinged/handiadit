from django.db import models

class AuthoringDatesModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Question(AuthoringDatesModel):
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text

class Choice(AuthoringDatesModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
