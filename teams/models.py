from django.db import models

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=30)
    titles = models.IntegerField(blank=True, default=0, null=True)
    top_scorer = models.CharField(max_length=50)
    fifa_code = models.CharField(max_length=3, unique=True)
    first_cup = models.DateField(blank=True, null=True)

    def __repr__(self) -> str:
        id = self.id
        name = self.name
        code_fifa = self.fifa_code

        return f"<[{id}] {name} - {code_fifa}>"