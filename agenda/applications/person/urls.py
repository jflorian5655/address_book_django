from django.urls import path, re_path

from . import views


app_name = 'person_app'

urlpatterns = [
    path('people', views.ListPeopleView.as_view(), name='_list_person'),
    path('api/person/list/', views.ListAPIPeopleView.as_view()),
    path('api/person/create/', views.CreatePersonAPIView.as_view()),
    path('api/person/detail/<pk>/', views.DetailPersonAPIView.as_view(), name='detail_person'),
    path('api/person/delete/<pk>/', views.DeletePersonAPIView.as_view()),
    path('api/person/update/<pk>/', views.UpdatePersonAPIView.as_view()),
    path('api/person/updatefields/<pk>/', views.UpdateFieldPersonAPIView.as_view()),
    path('api/person/list2/', views.List2APIPeopleView.as_view()),
    path('api/meeting/list/', views.MeetingListAPIView.as_view()),
    path('api/meeting/list-link/', views.MeetingListAPIViewLink.as_view()),
    path('api/person/list-pagination/', views.ListPaginationAPIPeopleView.as_view()),
    path('api/meeting/list-meeting-by-jobs/', views.MeetingsByPersonJobs.as_view()),

]

