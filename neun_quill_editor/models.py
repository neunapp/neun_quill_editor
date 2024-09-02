from django.db import models

class EditorField(models.TextField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def db_type(self, connection):
        # 
        return super().db_type(connection)