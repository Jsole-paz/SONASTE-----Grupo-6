from rest_framework import routers
from .viewsets import ArtistViewSet

router = routers.SimpleRouter()
router.register("api-artist",ArtistViewSet)