from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# other things associated with user
class Profile(models.Model):
    user = models.ForeignKey(User, primary_key=True)
    photoUrl = models.CharField(max_length=200)
    fbId = models.IntegerField()

    def __unicode__(self):
        return self.user.username


# generic book, movie, etc. Just has title
class Item(models.Model):
    title = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title

# links ItemList to all items in that list
class ItemListSet(models.Model):
    # belongs to exactly one item list
    itemList = models.OneToOneField("ItemList")
    items = models.ManyToManyField("Item")

    def __unicode__(self):
        return self.itemList.user.username + ":" + self.itemList.title + ":" +\
               self.items

# the lists the users create
class ItemList(models.Model):
    profile = models.ForeignKey(Profile)
    title = models.CharField(max_length=200)
    description = models.TextField()
    timeStamp = models.DateTimeField()
    itemListSet = models.OneToOneField(ItemListSet)

    def __unicode__(self):
        return self.user.username + ":" + self.title

# links user to the things a user rated
class UserItemSet(models.Model):
    profile = models.OneToOneField(Profile)
    items = models.ManyToManyField("Item")
    preference = models.BooleanField() # 0 is dislike, 1 is like

    def __unicode__(self):
        return self.user.username + self.items

################################################################
################# THINGS THAT EXTEND ITEMS #####################
################################################################
# multi-set/model inheritance

class Book(Item):
    author = models.CharField(max_length=200)
    # may require set-reference: genre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.title

class Song(Item):
    artist = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    year = models.IntegerField(max_length=200)
    # genre?

    def __unicode__(self):
        return self.title

class Movie(Item):
    director = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title

# comments belong to an itemlist
class ListComments(models.Model):
    # can only belong to one itemlist
    itemList = models.ForeignKey("ItemList")
    profile = models.ForeignKey(Profile)
    # for ordering comments
    timeStamp = models.DateTimeField()
    content = models.TextField()

    def __unicode__(self):
        return self.content
