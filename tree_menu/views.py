from django.shortcuts import render
from django.views.generic import TemplateView


class MenuView(TemplateView):
    template_name = "tree_menu/index.html"
