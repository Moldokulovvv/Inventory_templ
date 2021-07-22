from django.db.models import Q
from datetime import datetime

from django.views.generic import ListView

from akts.models import Akt
from .models import Category


def get_categories(request):
    categories = Category.objects.all()
    # if request.user.is_authenticated:
    #     acts = Akt.objects.filter(Q(sender=request.user) | Q(recipient=request.user))
    #     acts = acts.filter(time__lte=datetime.now())
    #     return {'categories': categories, 'acts': acts}
    return {'categories': categories}
