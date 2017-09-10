from django.conf.urls import url
from app.mascota.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete \
    ,MascotaList, MascotaUpdate, MascotaCreate, MascotaDelte

urlpatterns = [
    url(r'^$', index, name='index'),
    # url(r'^new$', mascota_view, name='mascota_crear'),
    url(r'^new$', MascotaCreate.as_view(), name='mascota_crear'),
    # url(r'^list$', mascota_list, name='mascota_listar'),
    url(r'^list$', MascotaList.as_view(), name='mascota_listar'),
    # url(r'^edit/(?P<id_mascota>\d+)/$', mascota_edit, name='mascota_editar'),
    url(r'^edit/(?P<pk>\d+)/$', MascotaUpdate.as_view(), name='mascota_editar'),
    # url(r'^delete/(?P<id_mascota>\d+)/$', mascota_delete, name='mascota_eliminar'),
    url(r'^delete/(?P<pk>\d+)/$', MascotaDelte.as_view(), name='mascota_eliminar'),
]