from rest_framework import serializers
from .models import Task
from datetime import date

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('id', 'created_at')

    def validate_due_date(self, value):
        if value is None:
            return value
        if value < date.today():
            raise serializers.ValidationError("due_date cannot be in the past.")
        return value
