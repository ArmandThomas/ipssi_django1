from django.contrib import admin

# Register your models here.

from .models import GameBoard, GameBoardCategory, GamePublisher

admin.site.register(GameBoard)
admin.site.register(GameBoardCategory)
admin.site.register(GamePublisher)
