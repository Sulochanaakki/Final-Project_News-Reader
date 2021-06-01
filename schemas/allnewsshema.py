from app import ma
from app.models.allnewsmodel import AllNewsModel

class AreaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AllNewsModel
        load_instance = True
        load_only = ("store",)
        include_fk = True