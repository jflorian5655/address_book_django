from django.shortcuts import render
from django.views.generic import ListView

from .models import Person, Meeting, Hobby
from .serializers import (
    PersonSerializer, ManualPersonSerializer, MeetingSerializer, PersonFullSerializer, MeetingSerializerLink,
    PersonPagination, CountMeetingByJobSerializer
)

from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, RetrieveUpdateAPIView
)


class ListPeopleView(ListView):
    """
    Vista de ejemplo para listar en HTML la lista de registros del modelo person.
    """

    template_name = 'person/list_person.html'
    context_object_name = 'people'

    def get_queryset(self):
        return Person.objects.all()


class ListAPIPeopleView(ListAPIView):
    """
    Vista de ejemplo para listar en json (REST-framework) la lista de registros del modelo person.
    """

    serializer_class = PersonFullSerializer  # PersonSerializer

    def get_queryset(self):
        return Person.objects.all()


class CreatePersonAPIView(CreateAPIView):
    """
    Vista para crear nuevo registro en el modelo person, mediante un servicio REST
    """

    serializer_class = PersonSerializer


class DetailPersonAPIView(RetrieveAPIView):
    """
    Vista para ver el detaale de un registro del modelo person, mediante un servicio REST
    """

    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class DeletePersonAPIView(DestroyAPIView):
    """
    Vista para borrar un registro del modelo person, mediante un servicio REST
    """

    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class UpdatePersonAPIView(UpdateAPIView):  # Este tipo de Update es para  actualizar todos los campos de un registro.
    """
    Vista para actualizar todos los datos de un registro del modelo person, mediante un servicio REST. Todos los campos
    se deben actualizar.
    """

    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class UpdateFieldPersonAPIView(RetrieveUpdateAPIView):  # Este tipo de Update es para  actualizar datos selsccionados
    """
    Vista para actualizar todos los datos de un registro del modelo person, mediante un servicio REST. Sin la necesidad
    de actualzilar todos los campos del registro.
    """

    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class List2APIPeopleView(ListAPIView):
    """
    Vista de  ejemplo para listar lo registros del modelo person, mediante  un servicio REST, utilizando un serializador
    desarrollado manualmente: ManualPersonSerializer
    """
    serializer_class = ManualPersonSerializer

    def get_queryset(self):
        return Person.objects.all()


class MeetingListAPIView(ListAPIView):
    """
    Vista para listar los registros del modelo meeting, mediante  un servicio REST
    """

    serializer_class = MeetingSerializer

    def get_queryset(self):
        return Meeting.objects.all()


class MeetingListAPIViewLink(ListAPIView):
    """
    Vista para listar los registros del modelo meeting, mediante  un servicio REST. Cargando los registros de la
    relación person, mediante un link.
    """

    serializer_class = MeetingSerializerLink

    def get_queryset(self):
        return Meeting.objects.all()


class ListPaginationAPIPeopleView(ListAPIView):
    """
    Vista para listar lo registros del modelo person, mediante  un servicio REST, utilizando un serializador de soporte
    para realizar la paginación de registros: PersonPagination
    """

    serializer_class = PersonFullSerializer
    pagination_class = PersonPagination

    def get_queryset(self):
        return Person.objects.all()


class MeetingsByPersonJobs(ListAPIView):
    """
    Vista para listar lo cantidad de reuniones  con personas de ada trabajo , mediante  un servicio REST, utilizando un
    manager como consulta.
    """

    serializer_class = CountMeetingByJobSerializer

    def get_queryset(self):
        return Meeting.objects.number_of_meetings_by_job()





