from django.db import models

# Create your models here.
from django.contrib.auth.models import User


def setup():
    userA = User.objects.create(username="D", password="B")
    userB = User.objects.create(username="E", password="B")
    userC = User.objects.create(username="F", password="B")
    profA=Profile.objects.create(user=userA, fbId=1)
    profB=Profile.objects.create(user=userB, fbId=2)
    profC=Profile.objects.create(user=userC, fbId = 3)
    a=Item.objects.create(ASIN="1", title = "A Roast beef")
    b=Item.objects.create(ASIN="2", title = "Some chicken")
    c=Item.objects.create(ASIN="3", title = " A Pizza")
    d=ItemPreference.objects.create(item=a, preference = True)
    e=ItemPreference.objects.create(item=b, preference = True)
    f=ItemPreference.objects.create(item=c, preference = True)
    g=ItemPreference.objects.create(item=a, preference = False)
    h=ItemPreference.objects.create(item=b, preference = False)
    i=ItemPreference.objects.create(item=c, preference = False)
    UserItemSet.objects.create(profile=profA, itemPreference = d)
    UserItemSet.objects.create(profile=profA, itemPreference = e)
    UserItemSet.objects.create(profile=profA, itemPreference = i)
    UserItemSet.objects.create(profile=profB, itemPreference = d)
    UserItemSet.objects.create(profile=profB, itemPreference = e)
    UserItemSet.objects.create(profile=profB, itemPreference = f)
    UserItemSet.objects.create(profile=profC, itemPreference = g)
    UserItemSet.objects.create(profile=profC, itemPreference = h)
    UserItemSet.objects.create(profile=profC, itemPreference = f)
    


# other things associated with user
class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    photoUrl = models.CharField(max_length=200)
    fbId = models.IntegerField()

    def __unicode__(self):
        return str(self.user.password) + self.user.username
	
	"""
	def __eq__(self, profile):
		if self == profile: 
			return True
		if user = profile.user and fbId = profile.fbId:
			return True
			
	def __ne__(self, profile):
		return not self.__eq__(profile)
	"""
	
# generic book, movie, etc. Just has title
class Item(models.Model):
    ASIN = models.CharField(max_length=200, primary_key=True)
    title = models.CharField(max_length=200)
    def __unicode__(self):
        return str(self.ASIN) + ":" + str(self.title)

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

class ItemPreference(models.Model):
    item = models.ForeignKey("Item")
    preference = models.BooleanField() # 0 is dislike, 1 is like
    
    def __unicode__(self):
	return self.item.title + ":" + str(self.preference)
	
# links user to the things a user rated
class UserItemSet(models.Model):
    profile = models.ForeignKey(Profile)
    itemPreference = models.ForeignKey("ItemPreference")

    def __unicode__(self):
        return self.profile.user.username

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
