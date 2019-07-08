from rest_framework import serializers
from .models import *


class RuleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Rules
		fields = ('id', 'name', 'operator', 'value')

class WorkFlowSerializer(serializers.ModelSerializer):
	rule = RuleSerializer(many=True)
	class Meta:
		model = WorkFlow
		fields = ('name', 'condition','rule')

class ProcessSerializer(serializers.ModelSerializer):
	workflow = WorkFlowSerializer()
	class Meta:
		model = Process
		fields = ('name', 'origin_node', 'destination_node', 'workflow')		