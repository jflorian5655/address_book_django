from .models import Person, Meeting, Hobby

from rest_framework import serializers, pagination


class PersonSerializer(serializers.ModelSerializer):
    """
    Serializador básico para todos los campos del del modelo Person. Agregando uno nuevo que no se encuentra dentro del
    modelo: active
    """

    active = serializers.BooleanField(default=False)  # Se puede agregar un campo adicional que no exista en el modelo

    class Meta:
        model = Person
        fields = '__all__'  # ('id', 'full_name', 'job', 'email', 'phone')  # Campos a serializar (query_set to json)


class HobbySerializer(serializers.ModelSerializer):
    """
    Serializador básico para el modelo Hobby para todos los campos del modelo Hobby.
    """

    class Meta:
        model = Hobby
        fields = '__all__'  # ('id', 'full_name', 'job', 'email', 'phone')  # Campos a serializar (query_set to json)


class PersonFullSerializer(serializers.ModelSerializer):
    """
    Serializador para los campos del modelo Person, especificando en json los datos que se encuntran según la relación
    person-hobbies.
    """

    hobbies = HobbySerializer(many=True)  # el atributo many solo se pone cuando una relación es ManyToMany.

    class Meta:
        model = Person
        fields = ('id', 'full_name', 'job', 'email', 'phone', 'hobbies')  # Campos a serializar (query_set to json)


class MeetingSerializer(serializers.ModelSerializer):
    """
    Serializador para los campos del modelo meeting, agregando un campo nuevo que no  existe en el midelo: full_date,
    apartir de campos existentes en el modelo.
    También se especifican los datos en json que se encuantra en la relación meeting-person.
    """

    full_date = serializers.SerializerMethodField()  # Nuevo campo a partir de campos existentes (date_meet, tine)
    person = PersonFullSerializer()  # json de Meeting con todos lo datos de las reuniones y de las personas

    class Meta:
        model = Meeting
        fields = ('id', 'date_meet', 'time', 'subject', 'full_date', 'person')

    def get_full_date(self, obj):
        """
        Concatenar la fecha y la hora del registro y crear un campo nuevo: full_date
        :param obj: registro
        :return: 'date_meet -- time'
        """
        return str(obj.date_meet) + ' -- ' + str(obj.time)


class MeetingSerializerLink(serializers.HyperlinkedModelSerializer):
    """
    Serializador para los campos del modelo meeting. También se especifican los datos en un link que se encuantra en la
    relación meeting-person.
    """

    class Meta:
        model = Meeting
        fields = ('id', 'date_meet', 'time', 'subject', 'person')
        extra_kwargs = {
            'person': {'view_name': 'person_app:detail_person', 'lookup_field': 'pk'}
        }


class PersonPagination(pagination.PageNumberPagination):
    """
    Serializador de soporte para agregar paginación a unn  selizador con una consulta. page_size: registros por página
    max_page_size: registros totales cargados en memoría.
    """
    page_size = 10
    max_page_size = 100


class CountMeetingByJobSerializer(serializers.Serializer):
    """
    Serializador manuel para el manager number_of_meetings_by_job, para saber la cantdad de reuniones  con personas de
    cada trabajo.
    """

    person__job = serializers.CharField()
    quantity = serializers.IntegerField()


class ManualPersonSerializer(serializers.Serializer):
    """
    Serializador para el modelo person, armado manualemnte, con cada campo a mostrar en json.
    """

    id = serializers.IntegerField()
    full_name = serializers.CharField()
    job = serializers.CharField()
    email = serializers.CharField()
    phone = serializers.CharField()
    active = serializers.BooleanField(default=False)  # Este campo no existe en el modelo, se puede pasar sin problemas.








