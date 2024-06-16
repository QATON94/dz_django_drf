from rest_framework import serializers

from materials.models import Course, Lesson
from materials.validators import ValidateLink
from users.models import Subscriptions


class CourseSerializer(serializers.ModelSerializer):
    """курс"""

    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):
    """урок"""

    class Meta:
        model = Lesson
        fields = "__all__"


class LessonCreateSerializer(serializers.ModelSerializer):
    """Создание урока"""

    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [ValidateLink(field='link')]


class CourseAndNumbersLessonsSerializer(serializers.ModelSerializer):
    """Курсы с подсчетом кол-ва уроков"""

    lesson_count = serializers.SerializerMethodField()
    subs = serializers.SerializerMethodField()

    def get_lesson_count(self, obj):
        lesson_count = Lesson.objects.filter(course=obj).count()
        return lesson_count

    def get_subs(self, obj):
        subs_check = Subscriptions.objects.filter(course=obj)
        if subs_check:
            subs = 'Подписка оформлена'
        else:
            subs = 'Подписка не оформлена'
        return subs

    class Meta:
        model = Course
        fields = "__all__"


class LessonsInCourseSerializer(serializers.ModelSerializer):
    """Выводит курс, список уроков и кол-во уроков"""

    lessons = serializers.StringRelatedField(many=True)
    lesson_count = serializers.SerializerMethodField()

    def get_lesson_count(self, obj):
        lesson_count = Lesson.objects.filter(course=obj).count()
        return lesson_count

    class Meta:
        model = Course
        fields = ['name', 'description', 'lessons', 'lesson_count']
