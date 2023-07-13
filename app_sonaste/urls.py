from django.urls import path
from .router import router


from .views import      UserListView   \
                    ,   UserCreateView \
                    ,   UserDetailView \
                    ,   UserUpdateView \
                    ,   UserDeleteView

app_name = "sonaste"

urlpatterns = [
    path("", UserListView.as_view(), name="all"),
    path("create/", UserCreateView.as_view(), name="create"),
    path("<int:pk>/detail/", UserDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", UserUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", UserDeleteView.as_view(), name="delete")
]

urlpatterns += router.urls