from sqlalchemy.ext.automap import automap_base
from serve import db

class Province(object):
    pass

class Franchise(object):
    pass

class Model(object):
    @classmethod
    def ddo(self):
        Base = automap_base()
        Base.prepare(db.engine, reflect=True)
        return Base