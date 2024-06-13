from rest_framework import serializers

from materials.models import Course, Lesson


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


class NumbersLessonsSerializer(serializers.ModelSerializer):
    """Курс с подсчетом кол-ва уроков"""

    lesson_count = serializers.SerializerMethodField()

    def get_lesson_count(self, obj):
        lesson_count = Lesson.objects.filter(course=obj).count()
        return lesson_count

    class Meta:
        model = Course
        # fields = ['name', 'description', 'picture', 'lesson_count']
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
