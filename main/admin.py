from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from django import forms
from main.models import *





class InventAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Invent
        fields = '__all__'

@admin.register(Invent)
class InventAdmin(admin.ModelAdmin):
    form = InventAdminForm



admin.site.register(Category)


