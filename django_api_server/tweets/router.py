from rest_framework import routers

from .views import TweetsViewSet


router = routers.DefaultRouter()
router.register("tweets", TweetsViewSet)
