from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Team, Player
from .serializers import TeamSerializer, PlayerSerializer

class Biding(generics.RetrieveUpdateDestroyAPIView):
    def update(self, request, *args, **kwargs):
        try:
            team_id = request.data.get("team_id")
            player_id = request.data.get("player_id")
            selling_price = float(request.data.get("selling_price"))  # Convert to integer

            team = Team.objects.get(id=team_id)
            player = Player.objects.get(id=player_id)

            # Check if the player is already sold
            if player.sold_to:
                return Response({"error": "Player is already sold"}, status=status.HTTP_400_BAD_REQUEST)

            # Check if the team has enough funds
            if team.funds_left < selling_price:
                return Response({"error": "Not enough funds"}, status=status.HTTP_400_BAD_REQUEST)

            # Update the player's final price and sold_to field
            player.final_price = selling_price
            player.sold_to = team
            player.save()

            # Update the team's funds_left field
            team.funds_left -= selling_price
            team.save()

            # Serialize updated data and return
            player_serializer = PlayerSerializer(player)
            team_serializer = TeamSerializer(team)

            return Response({"player": player_serializer.data, "team": team_serializer.data})
        except Team.DoesNotExist:
            return Response({"error": "Team not found"}, status=status.HTTP_404_NOT_FOUND)
        except Player.DoesNotExist:
            return Response({"error": "Player not found"}, status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response({"error": "Invalid selling price format"}, status=status.HTTP_400_BAD_REQUEST)
