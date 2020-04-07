from django.shortcuts import render, get_object_or_404

from .models import *


class ObjectDetailsMixin:
    model = None
    template = None

    def get(self, request, slug):
        object = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): object})

