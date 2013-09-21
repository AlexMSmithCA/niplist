from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, primary_key=True)
    photoUrl = models.CharField(max_length=200)
    fbId = models.IntegerField()

    def __unicode__(self):
	return self.user.username


class Item(models.Model):
    title = models.CharField(max_length=200)

    def __unicode__(self):
	return self.title

class ItemListSet(models.Model):
    itemList = models.OneToOneField("ItemList")
    items = models.ManyToManyField("Item")

    def __unicode__(self):
	return self.itemList.user.username + ":" + self.itemList.title + ":" +\
               self.items

class ItemList(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    description = models.TextField()
    timeStamp = models.DateTimeField()
    #itemListSet = models.OneToOneField(ItemListSet)

    def __unicode__(self):
	return self.user.username + ":" + self.title

class UserItemSet(models.Model):
    items = models.ManyToManyField("Item")
    user = models.OneToOneField(User)
    preference = models.BooleanField()

    def __unicode__(self):
	return self.user.username + self.items
    


class Book(Item):
    author = models.CharField(max_length=200)
    # may require set-reference: genre = models.CharField(max_length=200)
    
    def __unicode__(self):
	return self.title

class Song(Item):
    artist = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    year = models.IntegerField(max_length=200)
    # genre = models.CharField(max_length

    def __unicode__(self):
	return self.title    

class Movie(Item):
    director = models.CharField(max_length=200)

    def __unicode__(self):
	return self.title

class ListComments(models.Model):
    itemList = models.ForeignKey("ItemList")
    user = models.ForeignKey(User)
    timeStamp = models.DateTimeField()
    content = models.TextField()

    def __unicode__(self):
	return self.content
    
