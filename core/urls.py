from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import BookViewSet

router = DefaultRouter()
router.register(r"books", BookViewSet, basename="book")

urlpatterns = [
    # JWT endpoints
    path(
        "token/", TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),  # POST /api/token/
    path(
        "token/refresh/", TokenRefreshView.as_view(), name="token_refresh"
    ),  # POST /api/token/refresh/
]

urlpatterns += router.urls  # incluye /api/books/
