from rest_framework.views import APIView, Response, Request, status
from teams.models import Team
from django.forms.models import model_to_dict
from utils import data_processing


class TeamView(APIView):
    def post(self, request):
        team_data = request.data
        try:
            data_processing(team_data)
        except Exception as e:
            return Response({"error": e.message}, status.HTTP_400_BAD_REQUEST)

        team = Team.objects.create(
            name=team_data["name"],
            titles=team_data["titles"],
            top_scorer=team_data["top_scorer"],
            fifa_code=team_data["fifa_code"],
            first_cup=team_data["first_cup"],
        )
        return Response(model_to_dict(team), status.HTTP_201_CREATED)

    def get(self, request):
        teams = Team.objects.all()

        teams_dict = []

        for team in teams:
            m = model_to_dict(team)
            teams_dict.append(m)

        return Response(teams_dict, status.HTTP_200_OK)


class TeamFilteringById(APIView):
    def get(self, request, team_id):
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        team_dict = model_to_dict(team)
        return Response(team_dict, status.HTTP_200_OK)

    def patch(self, request, team_id):
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        for key, value in request.data.items():
            setattr(team, key, value)

        team.save()

        team_dict = model_to_dict(team)
        return Response(team_dict, status.HTTP_200_OK)

    def delete(self, request, team_id):
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
