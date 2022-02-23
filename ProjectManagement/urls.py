from django.urls import path
from . import views

urlpatterns = [

		#sa30
		path('projectAPI/',views.CR_ProjectApiView.as_view()),
        path('projectAPI/<int:pk>',views.U_ProjectApiView.as_view()),
        path('teamAPI/',views.CR_TeamApiView.as_view()),
        path('teamAPI/<int:pk>',views.U_TeamApiView.as_view()),
        path('teamMemberAPI/',views.CR_TeamMemberApiView.as_view()),
        path('teamMemberAPI/<int:pk>',views.U_TeamMemberApiView.as_view()),
        path('tasksAPI/',views.CR_Tasks.as_view()),
        path('tasksAPI/<int:pk>',views.U_Tasks.as_view()),

        path('home/',views.home,name='projectmanagementHome'),
        path('project/',views.project_view,name='project'),
        path('totalproject/',views.totalproject_view,name='totalproject'),
        path('inprogressproject/',views.inprogressproject_view,name='inprogressproject'),
        path('completedproject/',views.completedproject_view,name='completedproject'),
        path('projectupdate/<int:id>/',views.projectUpdate_view,name='projectupdate'),
        path('projectdelete/<int:id>/',views.projectDelete_view,name='projectdelete'),
        path('projectinfo/<int:id>/',views.projectInfo_view,name='projectinfo'),
        # path('<int:id>/',views.projectUpdate_view,name='projectupdate'),
        path('team/',views.team_view,name='team'),
        path('teamView/',views.teamView_view,name='teamView'),
        path('teamupdate/<int:id>/',views.teamUpdate_view,name='teamupdate'),
        path('teamdelete/<int:id>/',views.teamDelete_view,name='teamdelete'),

        path('teamember/',views.teammember_view,name='teammember'),
        path('teamemberView/',views.teammemberView_view,name='teammemberview'),
        path('teammemberUpdate/<int:id>/',views.teammemberUpdate_view,name='teammemberupdate'),
        path('teammemberdelete/<int:id>/',views.teammemberDelete_view,name='teammemberdelete'),

        path('task/',views.tasks_view,name='task'),
        path('addtaskinfopage/<str:membername>/<str:teamname>',views.addTaskInfoPage,name='addtaskinfopage'),
        path('taskView/',views.tasksView_view,name='taskView'),
        path('taskView/<str:projectname>',views.singletask_view,name='singletask'),
        path('singletaskstatus/<int:id>/',views.singletaskstatus,name='singletaskstatus'),
        path('taskUpdate/<int:id>/',views.taskUpdate_view,name='taskupdate'),
        path('taskdelete/<int:id>/',views.tasksDelete_view,name='taskdelete'),
        path('taskprogress/',views.taskprogressView_view,name='taskprogress'),
        path('taskprogressUpdate/<int:id>/',views.taskprogressUpdate_view,name='taskprogressupdate'),




        # path('mail',views.index),

         path('BO/',views.BOListView.as_view(),name='details'),
        path('BO/<pk>/',views.BOView.as_view(),name='put'),
         path('Project/',views.ProjectListView.as_view(),name='details'),
        path('Project/<pk>/',views.ProjectView.as_view(),name='put'),
         #path('Team/',views.TeamListView.as_view(),name='details'),

    # path('Team/<name>/edit/',views.TeamUpdateAPIView.as_view(),name='put'),

        #path('',views.ProjectManagement,name='project')
        
]
