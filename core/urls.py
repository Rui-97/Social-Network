from django.urls import path
from . import views
from . import api

# I wrote this code 
urlpatterns = [
    path("", views.landing, name = "landing"),
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("home/<int:pk>", views.home,name="home"),
    path("profile/update/<int:pk>/", views.profile_update, name="profile_update"),
    path("profile/<int:pk>/", views.profile, name="profile"),
    path("profile/following/<int:pk>/", views.profile_following, name="profile_following"),
    path("profile/followers/<int:pk>/", views.profile_followers, name="profile_followers"),    
    path("search/", views.search, name="search"),
    path("delete_post/<int:pk>/", views.delete_post, name="delete_post"),
    
    path("api/index/", views.api_index, name="api_index"),
    path("api/users/", api.UsersList.as_view(), name="users_list_api" ),
    path("api/user/<int:pk>/", api.UserDetail.as_view(), name="user_detail_api" ),
    path("api/profiles/", api.ProfilesList.as_view(), name="profiles_list_api" ),
    path("api/profile/<int:user_id>/", api.ProfileByUserDetail.as_view(), name="profile_detail_api" ),
    path("api/posts/<int:user_id>", api.PostsByUserList.as_view(),name="posts_list_api")
]
# end of code I wrote
