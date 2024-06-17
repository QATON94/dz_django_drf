from rest_framework import serializers


class ValidateLink:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        url = dict(value).get(self.field)
        # if not (url.startswith('https://www.youtube.com/') or url in 'youtube.com'):
        if not ('youtube.com' in url or url.startswith('https://www.youtube.com/')):
            raise serializers.ValidationError("Ссылка на видео может быть только с youtube.com")
