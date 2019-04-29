# 問題1

## 開発環境構築

### 前提

- Python 3.7

### 必要なパッケージ

- Django 2.1.8
- djangorestframework
- django-rest-auth
- django-rest-swagger

```
$ pip install django==2.1.8, django-rest-auth, djangorestframework, django-rest-swagger
```

### 手順

```
$ git clone  
$ cd django_api_server  

# データベースの作成  
$ python manage.py migrate
```

## サーバ立ち上げ手順

```
$ python manage.py runserver
```

### アカウントの作成について

サーバ立ち上げ後アカウント作成用のページにアクセスし、作成することでログイン状態となる。  
ログインはそこからしかできない。  
[アカウント作成用](http://127.0.0.1:8000/account/)  
[ログインユーザ確認用](http://127.0.0.1:8000/account/info)

### エンドポイントの仕様
下記の問題2参照。具体的には以下。  

- [GET] /api/v1/tweets/  
一覧の取得  
ログイン時: 自分以外のユーザのツイートを取得  
非ログイン時: 全ツイートを取得(id順)  

- [POST] /api/v1/tweets/  
ログイン中のみデータをPost可能  
ログインしたユーザのTweetをDBに登録  

- [GET] /api/v1/tweets/{id}/  
idのtweetを1個だけ取得  

- [PUT] /api/v1/tweets/{id}/  
更新処理  
ただしログイン中、かつ自身のツイートのみ  

- [DELETE] /api/v1/tweets/{id}/  
削除処理  
ただしログイン中、かつ自身のツイートのみ  

## テスト実行手順

```
$ python manage.py test
```

# 問題2

- ### Swaggerによるドキュメント自動生成

Swagger SpecなしでRESTful APIのドキュメントを自動生成する。便利。  
サーバ立ち上げ後下記にアクセスすることで閲覧できる。  
URL: http://127.0.0.1:8000/swagger-docs/