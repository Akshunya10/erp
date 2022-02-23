from django.contrib import admin
from .models import *
import nested_admin

admin.site.register(Businessopportunity)
admin.site.register(Project)


class TasksInline(nested_admin.NestedTabularInline):
     model=Tasks
     extra=0
	
	

class TeamMemberInline(nested_admin.NestedTabularInline):
     model=TeamMember
     inlines=[TasksInline,]
     extra=0

    


class TeamAdmin(nested_admin.NestedModelAdmin):

	inlines = [TeamMemberInline,]

# class TeamMemberInline(admin.TabularInline):
#      model        =           TeamMember
#      extra         =         0

# class TasksInline(admin.TabularInline):
#      model        =           Tasks
#      extra         =         0

# class TeamMemberAdmin(admin.ModelAdmin):
#     inlines      =          [TasksInline]
#     class Meta():
#        model           =       TeamMember
#        fieldsets       =(
#            (None,
#            {
#                'fields': ('team_member','task_assigned','updates','task_deadline')
#            }
#        ),
#        )  

# class TeamAdmin(admin.ModelAdmin):
#    inlines      =          [TeamMemberInline]
#    class Meta():
#        model           =       Team
#        fieldsets       =(
#            (None,
#            {
#                'fields': ('project','team_lead','team_member','task_assigned','updates','task_deadline')
#            }
#        ),
#        )

admin.site.register(Team,TeamAdmin)
admin.site.register(TeamMember)
admin.site.register(Tasks)
