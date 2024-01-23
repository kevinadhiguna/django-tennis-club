from django.http import HttpResponse
from django.template import loader
from django.db.models import Q

from .models import Member

def members(request):
  members = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'members': members,
  }
  return HttpResponse(template.render(context, request))

def details(request, slug):
  member = Member.objects.get(slug=slug)
  template = loader.get_template('details.html')
  context = {
    'member': member
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  ### -- QuerySet Get -- ###

  members = Member.objects.all().values()

  # Return a specific column
  firstnames = Member.objects.values_list('firstname')
  
  ### ------------------ ###

  ### -- QuerySet Filter (for more: https://www.w3schools.com/django/django_queryset_filter.php) -- ###
  
  # Return particular rows
  emily_data = Member.objects.filter(firstname='Emily').values()
  refsnes_id2 = Member.objects.filter(lastname='Refsnes', id=2).values()
  
  # (1) [extended version]
  tobias_or_emil = Member.objects.filter(firstname='Emil').values() | Member.objects.filter(firstname='Tobias').values()
  # (2) [same with (1), but still common] 
  mesut_or_smith = Member.objects.filter(Q(firstname='Mesut') | Q(firstname='Smith')).values()

  # Field Lookups syntax
  member_whose_firstname_starts_from_l = Member.objects.filter(firstname__startswith='L').values() # <- ... WHERE firstname LIKE 'L%'
  ### --------------------- ###

  ### -- QuerySet Order By -- ###
  members_ordered_by_firstname = Member.objects.all().order_by('firstname').values() # SELECT * FROM members ORDER BY firstname;
  members_descendingly_ordered_by_firstname = Member.objects.all().order_by('-firstname').values() # SELECT * FROM members ORDER BY firstname DESC;

  # Multiple Order Bys
  members_multi_ordered_by = Member.objects.all().order_by('lastname', '-id').values() # SELECT * FROM members ORDER BY lastname ASC, id DESC;
  ### ----------------------- ###

  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Manggo'],
    'fav_food': ['Apple', 'Banana', 'Manggo'],
    'pricey_fruits': ['Grape', 'Tomato', 'Pineapple'],
    'firstname': 'Linus',
    'members': members,
    'greeting': 1,
    'eat_fruits': True,
    'day': 'Friday',
    'firstnames': firstnames,
    'emily_data': emily_data,
    'refsnes_id2': refsnes_id2,
    'tobias_or_emil': tobias_or_emil,
    'mesut_or_smith': mesut_or_smith,
  }
  return HttpResponse(template.render(context, request))
