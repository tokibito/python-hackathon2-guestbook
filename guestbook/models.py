# coding: utf8
from datetime import datetime

from django.db import models

class Greeting(models.Model):
    """
    ゲストブックのコンテンツのモデル
    """
    username = models.CharField(u'名前', max_length=30)
    content = models.TextField(u'書き込み内容', max_length=1000)
    create_at = models.DateTimeField(u'書き込み日時', default=datetime.now)

    def __unicode__(self):
        """
        モデルの文字列表現
        内容の改行を削除して先頭から20文字を返す
        """
        return ''.join(unicode(self.content).splitlines())[:20]

    class Meta:
        # ソート順
        ordering = ('-create_at',)
        # 単数形
        verbose_name = u'書き込み'
        # 複数形
        verbose_name_plural = u'書き込み'
