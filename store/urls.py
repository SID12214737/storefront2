from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views 

router = SimpleRouter()
router.register(prefix="products", viewset=views.ProductViewSet)
router.register('collections', views.CollectionViewSet)

# URLConf
urlpatterns = router.urls
