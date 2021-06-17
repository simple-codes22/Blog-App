from django.db import models
from django.utils.timezone import now

class Enquiry(models.Model):
    user_name = models.CharField(max_length=30, default="Anonymous")
    question = models.TextField(null=False, blank=False)
    date_posted = models.DateField(default=now, editable=False)

    def __str__(self):
        return f"<Question Posted By {self.user_name} at {self.date_posted}>"

class Answer(models.Model):
    user_name = models.CharField(max_length=30, default="Anonymous")
    answer = models.TextField(null=False, blank=False)
    to_question = models.ForeignKey(Enquiry, on_delete=models.CASCADE)
    date_posted = models.DateField(default=now, editable=False)

    def __str__(self):
        return f"<Answer to question asked by {to_question.user_name}, date posted: {self.date_posted}>"



# Create your models here.
