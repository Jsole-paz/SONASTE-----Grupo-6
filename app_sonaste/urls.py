from django.urls import path
from .router import router


from .views import      ArtistListView   \
                    ,   ArtistDetailView \
                    ,   ArtistCreateView \
                    ,   ArtistUpdateView \
                    ,   ArtistDeleteView

app_name = "sonaste"

urlpatterns = [
    path("", ArtistListView.as_view(), name="all"),
    path("create/", ArtistCreateView.as_view(), name="create"),
    path("<int:pk>/detail/", ArtistDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", ArtistUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", ArtistDeleteView.as_view(), name="delete")
]

urlpatterns += router.urls