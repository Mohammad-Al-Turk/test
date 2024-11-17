from django.db import models

# Create your models here.
class ShowManager(models.Manager):
  def basic_validation(self,post_data):
    errors = {}
    if len(post_data['title']) < 2 :
      errors['title'] = "Title must be at least 2 characters"
    if len(post_data['network']) < 3 :
      errors['network'] = "Network must be at least 3 characters"
    if len(post_data['description']) < 10 :
      errors['description'] = "description must be at least 10 characters"
    return errors
  
class Show(models.Model):
  title = models.CharField(max_length=20)
  network =models.CharField(max_length=10)
  released_date = models.DateField()
  description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = ShowManager()

def get_all_shows():
  return Show.objects.all()

def get_show_by_id(id):
  return Show.objects.get(id=id)

def create_show(data):
  title = data["title"]
  network = data['network']
  released_date = data['released_date']
  description = data['description']
  Show.objects.create(title=title, network=network, released_date=released_date, description = description)



def destroy_show(id):
  show = Show.objects.get(id=id)
  show.delete()
  return show


def update_show(data):
  id = int(data['id'])
  c=Show.objects.get(id=id)
  c.title = data['title']
  c.description = data['description']
  c.network = data['network']
  c.released_date = data['released_date']
  c.save()