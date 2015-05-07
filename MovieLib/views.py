from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from MovieLib.models import Movie
from MovieLib.models import todo
from MovieLib.forms import MovieMixin
from django.core.urlresolvers import reverse

# Create your views here.
class IndexView(ListView):
    template_name = 'index.html'
    model = todo

class CreateView(CreateView):
	template_name = 'create.html'
	model = todo
	fields = ['What','Deadline','Done']
	success_url = '/'	
	
class UpdateView(UpdateView):
	template_name = 'update.html'
	model = todo
	fields =  ['What','Deadline','Done']
	success_url = '/'

class DeleteView(MovieMixin, DeleteView):
    template_name = 'delete_confirm.html'
    success_url = '/'
	
class ImpressumView(ListView):
    template_name = 'impressum.html'
    model = todo