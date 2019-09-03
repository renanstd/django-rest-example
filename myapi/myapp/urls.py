from . import views
from django.urls import path

urlpatterns = [
    path('musics/', views.MusicList.as_view(), name='music-list'),
    path('music/<int:pk>', views.MusicDetail.as_view(), name='music-detail'),

    path('albuns/', views.AlbumList.as_view(), name='album-list'),
    path('album/<int:pk>', views.AlbumDetail.as_view(), name='album-detail'),

    path('bands/', views.BandList.as_view(), name='bands-list'),
    path('band/<int:pk>', views.BandDetail.as_view(), name='band-detail'),

    path('members/', views.MemberList.as_view(), name='member-list'),
    path('member/<int:pk>', views.MemberDetail.as_view(), name='member-detail'),
]
