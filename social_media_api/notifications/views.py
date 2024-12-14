from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .models import Notification
from rest_framework import status


class NotificationListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        notifications = Notification.objects.filter(recipient=request.user).order_by(
            "-timestamp"
        )
        unread_notifications = notifications.filter(read=False)

        # Serialize notifications (basic example)
        data = [
            {
                "id": n.id,
                "actor": n.actor.username,
                "verb": n.verb,
                "target": str(n.target),
                "timestamp": n.timestamp,
                "read": n.read,
            }
            for n in notifications
        ]

        return Response({"notifications": data}, status.HTTP_200_OK)
