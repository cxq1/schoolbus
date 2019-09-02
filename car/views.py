import datetime
import time

from django.conf import settings
from django.core.cache import cache
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import FormMixin, FormView

from car.form import PathForm, QueryShfitForm, OrderForm
from .tasks import send_email_by_celery
from car.models import Car,Autoshift,CarAndShift,PathType

class DealDue(FormView):
    template_name = 'car/order_confirm.html'
    form_class = OrderForm
    
    def post(self, request, *args, **kwargs):
        self.handle_due()
        return super(DealDue, self).post(request,args,kwargs)
    def get(self, request, *args, **kwargs):
        return super(DealDue, self).get(request,args,kwargs)
        
    def handle_due(self):
            increase_due = False
            shift_id = self.request.POST.get('shift_id')
            shift = Autoshift.objects.filter(id=shift_id)[0]
            due_key = 'due:%s:%s' % (str(datetime.date.today()), self.request.path)

            if not cache.get(due_key):
                increase_due = True
                cache.set(due_key, 1, 60)
            if increase_due:
                if self.request.user.is_authenticated:

                    due = CarAndShift()
                    due.shift = shift

                    due.user = self.request.user
                    due.due_num = 1
                    due.created_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    due.save()
                    # self.send_email()
                else:
                    pass  # 返回登录页面
    def get_context_data(self, **kwargs):
        context= super(DealDue, self).get_context_data(**kwargs)
        # car_num= self.request.POST.get('car_num')
        # path=self.request.POST.get('path')
        # shift_id= self.request.POST.get('shift_id')
        # context.update({
        #     'car_num':car_num,
        #     'path':path,
        #     'shift_id':shift_id,
        # })
        time_flag =False
        now_time = datetime.datetime.strftime(datetime.datetime.today(), "%Y-%m-%d")
        try:
            shift_id = self.request.POST.get('shift_id')
            self.request.session['shift_id']=shift_id
            if shift_id ==None and self.request.session['shift_id']!=None:
                shift_id = self.request.session['shift_id']
            shift = Autoshift.objects.filter(id=shift_id)[0]

            end_time = datetime.datetime.strftime(shift.times + datetime.timedelta(days=3), "%Y-%m-%d")
            time_flag = now_time > end_time
        except:
            pass

        # if self.request.session['due_num']>shift.car.
        # 创建预约


        due = CarAndShift.objects.filter(user=self.request.user)  # 差一个user
        due.time_flag = time_flag
        context['due'] = due

        context['now_time'] = now_time

        return context

class QueryShift(FormView):
    template_name = 'car/ticketlist.html'
    form_class = QueryShfitForm

    def post(self, request, *args, **kwargs):
        return super(QueryShift, self).post(request,args,kwargs)
    def get_context_data(self, **kwargs):
        context= super(QueryShift, self).get_context_data()
        pathName= self.request.POST.get('fromStation')
        startDate = self.request.POST.get('start_date')
        carType= self.request.POST.get('car_type')
        if startDate != "":
            startDate= datetime.datetime.strptime(startDate,"%Y-%m-%d")


        path = PathType.objects.filter(path_name=pathName)[0]

        #
        # print(datetime.datetime(2019, 10, 17))
        shifts= Autoshift.objects.filter(path=path)
        if carType!=None :
            shifts= shifts.filter(car__car_type=carType)
        print(startDate)
        if startDate !=None:
            shifts = shifts.filter(times__gt=startDate)
        due_num = CarAndShift.objects.count()
        context.update({
            'path':path,
            'shifts':shifts,
            'due_num':due_num,
        })
        return context

class TicketList(FormView):
    template_name = "car/ticketlist.html"
    form_class =PathForm

    def post(self, request, *args, **kwargs):
        response = super(TicketList, self).post(request,args,kwargs)
        # self.request.session['path']=self.request.POST.get("dropdown")
        return response

    def get_context_data(self, **kwargs):
        context= super(TicketList, self).get_context_data(**kwargs)
        context['path'] = self.request.POST.get("dropdown")

        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset

class CancelDueView(TemplateView):
    template_name = 'car/due_center.html'

    def get(self, request, *args, **kwargs):
        response = super(CancelDueView, self).get(request,*args,**kwargs)
        due_id = kwargs.get('due_id')
        if due_id!= None:
            CarAndShift.objects.get(pk=due_id).delete()
        return redirect(reverse('deal-due'))

class AddDueView(TemplateView):
    template_name = 'car/due_center.html'

    def get(self, request, *args, **kwargs):
        response = super(AddDueView, self).get(request,*args,**kwargs)

        self.handle_due()

        return response

    def send_email(self):
        shift_id = self.request.session['shift_id']
        shift = Autoshift.objects.filter(id=shift_id)[0]

        subject = '预约消息'
        html_content = '<p>您已经预约了' + str(shift.times) + '车，请记得及时上车</p>'
        send_from = settings.DEFAULT_FROM_EMAIL
        email = self.request.user.email
        to_list = [email,]
        send_email_by_celery.delay(subject, html_content, send_from, to_list)

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
                # self.send_email()
            else:
                pass #返回登录页面

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        shift_id= self.request.session['shift_id']
        shift = Autoshift.objects.filter(id=shift_id)[0]
        # if self.request.session['due_num']>shift.car.
        #创建预约
        now_time= datetime.datetime.strftime(datetime.datetime.today(),"%Y-%m-%d")
        end_time = datetime.datetime.strftime(shift.times+datetime.timedelta(days=3),"%Y-%m-%d")
        time_flag = now_time>end_time

        due =CarAndShift.objects.filter(shift=shift,user=self.request.user)#差一个user
        due.time_flag = time_flag
        context['due']=due

        context['now_time'] =now_time

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
    # template_name = 'car/shift_list.html'
    template_name="center.html"
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