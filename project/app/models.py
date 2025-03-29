from django.db import models
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views import View
from django import forms

# Models
class Rack(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    rack = models.ForeignKey(Rack, on_delete=models.CASCADE)
    datetime_added = models.DateTimeField(auto_now_add=True)
    unit = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name