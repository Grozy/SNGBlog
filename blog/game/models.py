#encoding: utf-8

from django.db import models
from django.contrib import admin

# Create your models here.
class GameInfo(models.Model):
    title = models.CharField(r'游戏名称', max_length = 150)
    body = models.TextField(r'详情')
    timestamp = models.DateTimeField(r'更新日期')

    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name = "游戏信息"
        verbose_name_plural = "游戏信息列表"

class GameInfoDisplay(admin.ModelAdmin):
    list_display = ('title', 'body')

admin.site.register(GameInfo, GameInfoDisplay)
