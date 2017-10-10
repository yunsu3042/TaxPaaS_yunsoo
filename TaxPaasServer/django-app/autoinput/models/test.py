from django.db import models

__all__ = ('Reporter', 'Article' )


class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Article(models.Model):
    reporter = models.ForeignKey(Reporter,
                                 blank=True,
                                 on_delete=models.CASCADE)
    headline = models.CharField(max_length=100)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('headline', )


class Car(models.Model):
    name = models.CharField(max_length=30)


class Engine(models.Model):
    name = models.CharField(max_length=30)
    car = models.OneToOneField(Car)
