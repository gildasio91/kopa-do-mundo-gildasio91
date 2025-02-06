from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Team
from django.forms.models import model_to_dict
from utils import data_processing
from json.decoder import JSONDecodeError
from django.http import JsonResponse


# Create your views here.


class TeamView(APIView):
    def get(self, request):
        teams = Team.objects.all()

        teams_dict = []

        for team in teams:
            t = model_to_dict(team)
            teams_dict.append(t)

        return Response(teams_dict, status.HTTP_200_OK)
    
    def post(self, request):
            team_data = request.data 
            data_processing(team_data)

            team = Team.objects.create(**team_data)

            return Response(model_to_dict(team), status.HTTP_201_CREATED)

    
class TeamDetailView(APIView):
            def get(self, request, team_id):
                try:
                    team = Team.objects.get(id=team_id)
                except Team.DoesNotExist:  
                    return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)
                
                team_dict = model_to_dict(team)

                return Response(team_dict, status.HTTP_200_OK)
            
            def delete(self, request, team_id):
                try:
                    team = Team.objects.get(id=team_id)
                except Team.DoesNotExist:
                    return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)
                
                team.delete()

                return Response(status=status.HTTP_200_OK)
                   
            def patch(self, request, team_id):
                try:
                    team = Team.objects.get(id=team_id)

                except Team.DoesNotExist:  
                    return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)
            
                for k, v in request.data.items():
                    setattr(team, k, v)

                team.save()
                return Response(model_to_dict(team), status.HTTP_200_OK)
