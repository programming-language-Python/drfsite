import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from women.models import Women


# короткая форма записи
class WomenSerializer(serializers.ModelSerializer):
    # user - атрибут из модели. Заполняем следующим образом
    user = serializers.HiddenField(default=serializers.CurrentUserDefault)

    class Meta:
        model = Women
        # какие поля из БД будем возвращать клиенту
        # fields = ('title', 'content', 'cat')
        # все поля
        fields = '__all__'

# длинная форма записи
# class WomenSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#     # read_only = True - будут читаться при добавлении записи в БД.
#     # Поля становятся не обязательные для заполнения для серилизатора
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     cat_id = serializers.IntegerField()
#
#     # переопределяем методы
#     def create(self, validated_data):
#         return Women.objects.create(**validated_data)
#
#     # instance - ссылка на объект Women
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.content = validated_data.get('content', instance.content)
#         instance.time_update = validated_data.get('time_update', instance.time_update)
#         instance.is_published = validated_data.get('is_published', instance.is_published)
#         instance.cat_id = validated_data.get('cat_id', instance.cat_id)
#         instance.save()
#         # обязательно вернуть
#         return instance

# ДО
# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


# # сериализатор
# class WomenSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()

# def encode():
#     model = WomenModel('Angelina Jolie', 'Content: Angelina Jolie')
#     model_sr = WomenSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     # преобразует объект сериализации в байтовую json строку
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Angelina Jolie","content":"Content: Angelina Jolie"}')
#     data = JSONParser().parse(stream)
#     serializer = WomenSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)

# class WomenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Women
#         # Поля для сериализации. Поля, которые будут отправляться пользователю
#         fields = ('title', 'cat_id')
