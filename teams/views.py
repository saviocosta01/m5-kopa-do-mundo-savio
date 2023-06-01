from rest_framework.views import APIView
from rest_framework.response import Response
from teams.models import Team
from django.forms.models import model_to_dict
from utils import data_processing


class TeamView(APIView):
    def post(self, request):
        team_data = request.data
        try:
            data_processing(team_data)
        except Exception as e:
            return Response({"error": e.message}, 400)

        team = Team.objects.create(
            name=team_data["name"],
            titles=team_data["titles"],
            top_scorer=team_data["top_scorer"],
            fifa_code=team_data["fifa_code"],
            first_cup=team_data["first_cup"],
        )
        return Response(model_to_dict(team), 201)

    def get(self, request):
        teams = Team.objects.all()

        teams_dict = []

        for team in teams:
            m = model_to_dict(team)
            teams_dict.append(m)

        return Response(teams_dict, 200)
