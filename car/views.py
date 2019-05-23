import datetime
import time

from django.core.cache import cache
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, ListView, TemplateView
from car.models import Car,Autoshift,CarAndShift,PathType

class CancelDueView(TemplateView):
    template_name = 'car/due_center.html'

    def get(self, request, *args, **kwargs):
        response = super(CancelDueView, self).get(request,*args,**kwargs)
        due_id = kwargs.get('due_id')
        if due_id!= None:
            CarAndShift.objects.get(pk=due_id).delete()
        return redirect(reverse('due-center'))

class AddDueView(TemplateView):
    template_name = 'car/due_center.html'

    def get(self, request, *args, **kwargs):
        response = super(AddDueView, self).get(request,*args,**kwargs)

        self.handle_due()
        return response

    def handle_due(self):
        increase_due = False
        shift_id = self.request.session['shift_id']
        shift = Autoshift.objects.filter(id=shift_id)[0]
        due_key = 'due:%s:%s' % (str(datetime.date.today()), self.request.path)

        if not cache.get(due_key):
            increase_due = True
            cache.set(due_key, 1, 24 * 60 * 60)
        if increase_due:
            if self.request.user.is_authenticated:

                due = CarAndShift()
                due.shift = shift

                due.user = self.request.user
                due.due_num = 1
                due.created_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                due.save()
            else:
                pass #返回登录页面

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        shift_id= self.request.session['shift_id']
        shift = Autoshift.objects.filter(id=shift_id)[0]
        # if self.request.session['due_num']>shift.car.
        #创建预约

        due =CarAndShift.objects.filter(shift=shift,user=self.request.user)#差一个user
        context['due']=due

        return context



#汽车列表
class CarListView(ListView):
    model = Car
    template_name = 'car/car_list.html'
    context_object_name = 'cars'



    def get_queryset(self):
        queryset = super(CarListView, self).get_queryset()
        shift_id= self.kwargs.get('shift_id')
        self.request.session['shift_id'] =shift_id
        shift= Autoshift.objects.get(id=shift_id)
        path= self.request.session['path']

        queryset = shift.car.all()

        return queryset

    def get_context_data(self, **kwargs):
        shift_id = self.kwargs.get('shift_id')

        shift = Autoshift.objects.get(id=shift_id)
        due_num= CarAndShift.objects.filter(shift=shift).count()
        self.request.session['due_num']=due_num
        context = super().get_context_data(**kwargs)

        context.update({
            'due_num':due_num,
        })
        return context


#汽车班次
class ShiftListView(ListView):
    model = Autoshift
    template_name = 'car/shift_list.html'
    context_object_name = 'shifts'

    def get_context_data(self, **kwargs):
        context = super(ShiftListView, self).get_context_data(**kwargs)
        pathes = PathType.objects.all()

        context.update({
            'pathes': pathes,
        })
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        path_name = self.request.GET.get('dropdown','')

        path=None
        self.request.session['path'] = path
        # path = get_object_or_404(PathType,path_name=path_name)
        try:
            path= PathType.objects.filter(path_name=path_name)[0]
        except:
            print("err")
        print(path)
        if path!= None:
            return queryset.filter(path__path_name=path.path_name).all().distinct()
        else:
            return queryset

class CarDetailView(DetailView):
    model = Car
    template_name = 'car/car_detail.html'
    context_object_name = 'car'
    pk_url_kwarg = 'car_id'

    def get_context_data(self, **kwargs):
        context = super(CarDetailView, self).get_context_data(**kwargs)
        shifts= Autoshift.objects.filter(car=self.get_object())


        context.update({
            'shifts':shifts,
            'back':self.request.GET.get('from')
        }

        )
        return context


class ShiftDetail(DetailView):
    model = Autoshift
    template_name = 'car/car_shift_detail.html'
    context_object_name = 'shift'
    pk_url_kwarg = 'shift_id'

    def get_context_data(self, **kwargs):
        context = super(ShiftDetail, self).get_context_data(**kwargs)

        shift = Autoshift.objects.filter(pk=self.kwargs.get('shift_id'))[0]

        cars = shift.car.all()
        context.update({
            'cars':cars,
        })
        return context