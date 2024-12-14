from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from .serializers import UserRegistrationSerializer, UserProfileSerializer
from rest_framework import generics
from .models import CustomUser


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get(user=user)
            return Response(
                {"message": "Registration successful", "token": token.key},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        serializer = UserProfileSerializer(
            request.user, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id, *args, **kwargs):
        # Get the target user
        user_to_be_followed = self.queryset.filter(id=user_id).first()
        # Run some validations
        if not user_to_be_followed:
            return Response(
                {"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND
            )

        if user_to_be_followed:
            if user_to_be_followed == request.user:
                return Response(
                    {"detail": "You cannot follow yourself."}, status.HTTP_403_FORBIDDEN
                )
            # Add target to requesting user's following field
            request.user.following.add(user_to_be_followed.id)
            return Response(
                {
                    "detail": f"You have successfully followed {user_to_be_followed.username}"
                },
                status.HTTP_200_OK,
            )


class UnFollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id, *args, **kwargs):
        # Get the target user
        user_to_be_unfollowed = self.queryset.filter(id=user_id).first()
        # Run some validations
        if not user_to_be_unfollowed:
            return Response(
                {"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND
            )

        if user_to_be_unfollowed:
            if user_to_be_unfollowed == request.user:
                return Response(
                    {"detail": "You cannot unfollow yourself."},
                    status.HTTP_403_FORBIDDEN,
                )
            # Add target to requesting user's following field
            request.user.following.remove(user_to_be_unfollowed.id)
            return Response(
                {
                    "detail": f"You have successfully unfollowed {user_to_be_unfollowed.username}"
                },
                status.HTTP_200_OK,
            )
