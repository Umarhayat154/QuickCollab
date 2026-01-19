from rest_framework import serializers
from notes.models import Note


class NoteSerializer(serializers.ModelSerializer):
    author=serializers.ReadOnlyField(source='author.id')

    class Meta:
        model=Note
        fields=('id','title','content','is_public','author','created_at','updated_at')

    def validate(self, value):
        user = self.context['request'].user
        if Note.objects.filter(author=user, title=value).exists():
            raise serializers.ValidationError("Title must be unique as per author")
        return value
    