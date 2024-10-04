from django.db import models

# Create your models here.
title = models.CharField(max_length=200)
author = models.CharField(max_length=100)
publication_year = models.IntegerField()