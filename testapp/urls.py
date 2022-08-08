# pathをインポート
from django.urls import URLPattern, path
from . import views


urlpatterns = [
    #  <アプリケーション名>/indexのurlにアクセスすると
    #  viewsのindexのメソッドが呼ばれる(後述)
    #  nameにはurlの名称を記載
    path("", views.root, name="root"),
    path("index", views.index, name="index"),
]
