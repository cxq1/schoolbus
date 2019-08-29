import xadmin
from django.contrib import admin
from django.urls import path
from .views import CarListView,CarDetailView,ShiftDetail,ShiftListView,AddDueView,CancelDueView,TicketList,QueryShift,\
    DealDue

urlpatterns = [
    path('car_list/<int:shift_id>', CarListView.as_view(), name='car-list'),
    path('car_detail/<int:car_id>', CarDetailView.as_view(), name='car-detail'),
    path('shift_detail/<int:shift_id>',ShiftDetail.as_view(),name='shift-detail'),
    path('shift_list/',ShiftListView.as_view(),name='shift-list'),
    path('due_center/',AddDueView.as_view(),name='due-center'),
    path('cancel_due/<int:due_id>',CancelDueView.as_view(),name='cancel-due'),
    path('ticket_list/',TicketList.as_view(),name='ticket-list'),
    path("query_shift/",QueryShift.as_view(),name='query-shift'),
    path("deal_due",DealDue.as_view(),name='deal-due'),
]