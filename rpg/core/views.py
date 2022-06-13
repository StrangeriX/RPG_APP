from telnetlib import DET
from urllib import request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from . import models

class CharacterList(ListView):
    model = models.Character
    context_object_name = 'characters'

class CharacterCreate(CreateView):
    model = models.Character
    fields = ['name', 'race']
    success_url = reverse_lazy('attribute_form')

    def form_valid(self, form):
        new_attributes = models.Attribute.objects.create()
        form.instance.attributes = new_attributes
        form.instance.user = self.request.user
        return super(CharacterCreate, self).form_valid(form)

class CharacterDetail(DeleteView):
    model = models.Character
    context_object_name = 'character'
    template_name = 'core/character_detail.html'
    success_url = reverse_lazy('character_detail')
    

    def post(request):
        print("aaaaaaaaaaaaaaa")
