from django import forms
from django.core.exceptions import ValidationError
from .models import Tag


class TagForm(forms.Form):
    title = forms.CharField(max_length=50)
    slug = forms.CharField(max_length=50)

    title.widget.attrs.update({'class': 'form-control'})
    slug.widget.attrs.update({'class': 'form-control'})

    def save(self):
        return Tag.objects.create(title=self.cleaned_data['title'],
                                  slug=self.cleaned_data['slug'])

    def clean_slug(self):
        new_slug = self.cleaned_data.get('slug').lower()

        if new_slug == 'create':
            raise ValidationError('Slug cannot be "Create"')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('The slug "{}" is already exists'.format(new_slug))
        return new_slug
