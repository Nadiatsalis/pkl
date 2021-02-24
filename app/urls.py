from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    # path('check-tanggal', views.check_tanggal),
    path('<tambah-tanggal-merah', views.tanggal_merah_create, name='tambah-tanggal-merah'),
	path('<int:pk>/uraian', views.uraian, name='uraian'),
    path('tambah-spj', views.create_spj,name='tambah-spj'),
    path('edit-spj/<str:pk>', views.edit_spj,name='edit-spj'),
    path('delete-spj/<str:pk>', views.delete_spj,name='delete-spj'),
    path('', views.index, name='index'),
    path('home', views.home, name='home')
    # path('logout', views.logout_view)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)