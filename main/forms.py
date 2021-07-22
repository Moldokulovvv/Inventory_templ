from ckeditor.widgets import CKEditorWidget
from django import forms

from main.models import Invent


class AddInventForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Invent
        fields = ('title', 'serial_number', 'invent_number', 'image', 'description', 'category', )
