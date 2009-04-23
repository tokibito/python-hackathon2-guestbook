=====================================
Django Hack-a-thon Disc.8 ハンズオンA
=====================================

事前にインストールしておくもの
==============================

- Python 2.5
- Django 1.0

ゲストブックアプリを動かしてみよう
==================================

サンプルのゲストブックアプリケーションを動かしてみます。

startproject
------------

はじめに、アプリケーションを動作させるためのプロジェクトを作成します。

ターミナル(or コマンドプロンプト)から次のように入力します。

::

  django-admin.py startproject プロジェクト名

プロジェクト名は半角英数で入力してください。ハイフンとアンダースコアは利用できます。

プロジェクト名とアプリケーションの名前が同じにならないように注意してください。

日本語を含むパスでは、うまく動作しないことがあります。

これで、プロジェクト名のディレクトリが作成されます。

インストールの仕方によっては django-admin.py が django-admin になっているかもしれません。

プロジェクトの設定を行う
------------------------

プロジェクト内の settings.py を編集します。
編集項目は以下の通りです。

.. code-block:: python

  DATABASE_ENGINE = 'sqlite3' # データベースエンジンはSQLite3
  DATABASE_NAME = 'data.db' # データベースファイル
  TIME_ZONE = 'Asia/Tokyo' # タイムゾーンは東京
  LANGUAGE_CODE = 'ja' # 言語は日本語

アプリケーションを追加する
--------------------------

guestbook アプリケーションをプロジェクトのディレクトリにコピーします。
続いて settings.py の INSTALLED_APPS に guestbook を追加します。
一緒に Django の管理アプリケーションもインストールしておきます。

.. code-block:: python

  INSTALLED_APPS = (
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.sites',
      'django.contrib.admin', # これを追加
      'guestbook', # これを追加
  )

これでアプリケーションをプロジェクトに追加できました。

アプリケーションのURLを有効にする
---------------------------------

アプリケーションのURLを有効にするため、プロジェクト内の urls.py を編集します。
urls.py を次のように書き換えます。

.. code-block:: python

  from django.conf.urls.defaults import *
  
  from django.contrib import admin
  admin.autodiscover()
  
  urlpatterns = patterns('',
      (r'^admin/(.*)', admin.site.root),
      (r'.*', include('guestbook.urls')),
  )

データベースへ反映させる
------------------------

インストールしたアプリケーションのモデルをデータベースに反映させます。
ターミナルで以下のコマンドを実行します。

::

  python manage.py syncdb

管理ユーザの作成を聞かれた場合、作成しておいてください。

これでデータベースへの反映ができました。

開発用サーバを起動して動かしてみる
----------------------------------

開発用サーバを起動するには、ターミナルで以下のコマンドを実行します。

::

  python manage.py runserver

デフォルトでは 127.0.0.1:8000 で起動されます。

Webブラウザから、 http://127.0.0.1:8000/ へアクセスするとゲストブックアプリケーションを利用できます。

管理画面は http://127.0.0.1:8000/admin/ でアクセスできます。
