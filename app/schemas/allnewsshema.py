from app.config import ma, db
from app.models.allnewsmodel import AllNewsModel

class AllNewsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AllNewsModel
        load_instance = True
        load_only = ("store",)
        include_fk = True
