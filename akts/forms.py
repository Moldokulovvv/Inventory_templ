from datetime import datetime

from django import forms

from akts.models import Akt
from main.models import Invent


class ActForm(forms.ModelForm):


    class Meta:
        model = Akt
        fields = ('recipient', 'address', 'fio', 'position', 'inventory', )


    def clean_inventory(self):
        inventory = self.cleaned_data.get('inventory')
        for i in inventory.split(','):
            try:
                b = Invent.objects.get(invent_number=i)
            except:
                raise forms.ValidationError('Неправильно указаны данные')
        return inventory



class ActFormTime(forms.ModelForm):
    time = forms.DateTimeField(initial=datetime.now().strftime('%Y-%m-%d %H:%M'), required=False)
    created_at = forms.DateTimeField(initial=datetime.now().strftime('%Y-%m-%d %H:%M'), required=False)
    class Meta:
        model = Akt
        fields = ('recipient', 'address', 'fio', 'position', 'time', 'inventory', )


