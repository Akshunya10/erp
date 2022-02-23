from rest_framework import serializers
from .models import *






class BusinessopportunitySerializer(serializers.ModelSerializer):
    #upload_documents = serializers.FileField(max_length=None, use_url=True)
    class  Meta:
          model        =           Businessopportunity
          fields       =           '__all__'

class ProjectSerializer(serializers.ModelSerializer):
   # project_link = TeamSerializer(many=True)

    class Meta:
          model         =           Project
          fields        =          '__all__'


class TeamSerializer(serializers.ModelSerializer):
   class Meta:
         model         =           Team
         fields        =           '__all__'

class TeamMemberSerializer(serializers.ModelSerializer):
   class Meta:
         model         =           TeamMember
         fields        =           '__all__'

class TasksSerializer(serializers.ModelSerializer):
   class Meta:
         model         =           Tasks
         fields        =           '__all__'
    

#class ProjectSerializer(serializers.ModelSerializer):
#    project_link = TeamSerializer(many=True)

#    class Meta:
  #        model         =           Project
#          fields        =           #['project_name','description','start_date','project_deadline','owner','project_status','team_lead','project_link']


#    def create(self, validated_data):
 #       pts = validated_data.pop('project_link')
        # -------pts=project teams--------
  #      po = Project.objects.create(**validated_data)
        # --------po=project object--------------
    #    for pt in pts:
   #        Team.objects.create(project=po, **pt)
    #    return po

    #def update(self, instance, validated_data):
    #    pts= validated_data.pop('project_link')
    #    teams = (instance.project_link).all()
    #    teams = list(teams)
    #    instance.project_name = validated_data.get('project_name', instance.project_name)
    #   instance.description= validated_data.get('description', instance.description)
    #   instance.start_date = validated_data.get('start_date', instance.start_date)
    #    instance.project_deadline = validated_data.get('project_deadline', instance.project_deadline)
    #   instance.project_status = validated_data.get('project_status', instance.project_status)
     #   instance.owner = validated_data.get('owner', instance.owner)
      #  instance.team_lead = validated_data.get('team_lead', instance.team_lead)
       # instance.save()

        #for pt in pts:
         #   team = teams.pop(0)
          #  team.team_member= pt.get('team_member', team.team_member)
           # team.task_assigned = pt.get('task_assigned', team.task_assigned)
            #team.updates = pt.get('updates', team.updates)
            #team.task_deadline = pt.get('task_deadline', team.task_deadline)
            #team.save()
            #return instance
