from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect

from django.views.generic import ListView, DetailView


from main.forms import AddInventForm
from main.models import Invent, Category


class IndexPageView(ListView):
    model = Invent
    template_name = 'index.html'
    context_object_name = 'invents'


    def get_template_names(self):
        template_name = super(IndexPageView, self).get_template_names()
        search = self.request.GET.get('q')
        if search:
            template_name = 'search.html'
        return template_name



    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get('q')
        if search:
            context['invents'] = Invent.objects.filter(Q(title__icontains=search) | Q(invent_number__icontains=search) | Q(serial_number__icontains=search))

        else:
            context['invents'] = Invent.objects.all()

        return context




def CategoryDetail(request, slug, *args, **kwargs,):
    category = kwargs.get('slug', None)
    cats = Category.objects.get(slug=slug)
    invents = Invent.objects.filter(category_id=slug)

    paginator = Paginator(invents, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'category-detail.html', locals())


class InventDetailView(DetailView):
    model = Invent
    template_name = 'invent-detail.html'
    context_object_name = 'invent'




# class AddInventView(CreateView):
#     model = Invent
#     form_class = AddInventForm
#     template_name = 'add-invent.html'
#     success_url = reverse_lazy('home')

def add_invent(request):
    if request.method == 'POST':

        invent_form = AddInventForm(request.POST, request.FILES)
        if invent_form.is_valid():
            new_invent = invent_form.save(commit=False)
            new_invent.institution = request.user.institution
            new_invent.save()
            return redirect('home')


    else:
        invent_form = AddInventForm()

    return render(request, 'add-invent.html', locals())


def act_test(request):
    return render(request, 'act-test.html')



def reestr_test(request):
    return render(request, 'index.html')





