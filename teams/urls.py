from django.urls import path
from .views import TeamView, TeamFilteringById

urlpatterns = [
    path("teams/", TeamView.as_view()),
    path("teams/<int:team_id>/", TeamFilteringById.as_view()),
]
