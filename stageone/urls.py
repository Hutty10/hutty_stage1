from django.urls import path
from stageone.views import StageOneUserView

app_name = "stageone"

urlpatterns = [
    path("me/<int:pk>", StageOneUserView.as_view(), name="Stageoneuser"),
]
