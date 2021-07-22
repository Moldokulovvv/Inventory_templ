from datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import DetailView,ListView
from django.contrib import messages
from akts.forms import ActForm, ActFormTime
from akts.models import Akt
from main.models import Invent
from django.db.models import Q


class ActListView(ListView):
    model = Akt
    template_name = 'act-list.html'
    context_object_name = 'akts'

    def get_template_names(self):
        template_name = super(ActListView, self).get_template_names()
        search = self.request.GET.get('q')
        print(search)
        if search:
            template_name = 'act-list.html'
        return template_name


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        search = self.request.GET.get('q')
        if search:
            context['akts'] = Akt.objects.filter(Q(created_at__icontains=search))

        else:
            context['akts'] = Akt.objects.all()

        return context


def act_create(request):

    if request.method == 'POST':

        act_form = ActForm(request.POST)
        recip = request.POST.get('recipient')
        invent = request.POST.get('inventory')

        if int(recip) == request.user.id:
            messages.add_message(request, messages.ERROR, 'Нельзя указывать себя')
            return HttpResponseRedirect('')


        for i in invent.split(','):
            try:
                inv = Invent.objects.get(invent_number=i)
                if inv.institution != request.user.institution:
                    messages.add_message(request, messages.ERROR, 'Этот инвентарь не принадлежит вашему учреждению')
                    return HttpResponseRedirect('')
            except:
                continue




        if act_form.is_valid():
            act = act_form.save(commit=False)
            act.sender = request.user
            act.created_at = datetime.now().strftime('%Y-%m-%d %H:%M')
            act.save()
            a = act.inventory
            for i in a.split(','):
                b = Invent.objects.get(invent_number=i)
                b.act_number = act.id
                b.save()
            return redirect('acts')
    else:
        act_form = ActForm()

    return render(request, 'act-create.html', locals())






def act_create_time(request):

    if request.method == 'POST':
        act_form = ActFormTime(request.POST)
        recip = request.POST.get('recipient')
        invent = request.POST.get('inventory')

        if int(recip) == request.user.id:
            messages.add_message(request, messages.SUCCESS, 'Нельзя отправлять себе')
            return HttpResponseRedirect('')



        for i in invent.split(','):
            try:
                inv = Invent.objects.get(invent_number=i)
                if inv.institution != request.user.institution:
                    messages.add_message(request, messages.ERROR, 'Этот инвентарь не принадлежит вашему учреждению')
                    return HttpResponseRedirect('')
            except:
                continue

        if act_form.is_valid():
            act = act_form.save(commit=False)
            act.sender = request.user
            act.created_at = datetime.now().strftime('%Y-%m-%d %H:%M')
            act.save()
            a = act.inventory
            for i in a.split(','):
                b = Invent.objects.get(invent_number=i)
                b.act_number = act.id
                b.save()
            return redirect('acts')

    else:
        act_form = ActFormTime()

    return render(request, 'act-create.html', locals())




class ActDetailView(DetailView):
    model = Akt
    template_name = 'act-detail.html'
    context_object_name = 'akt'



class Test(DetailView):
    model = Akt
    template_name = 'test-pdf.html'
    context_object_name = 'act'

    def get_context_data(self, **kwargs):
        context = super(Test, self).get_context_data(**kwargs)
        obj = self.get_object()
        print(obj.id)
        context['objs'] = Invent.objects.filter(act_number=obj.id)
        return context
