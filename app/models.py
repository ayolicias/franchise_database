from serve import db
from app.base import Model

class ProvinceModel(object):
    def add(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    @classmethod
    def fetchOne(self):
        pass

    @classmethod
    def fetchAll(self):
        Province = self.ddo().classes.provinces
        sess = self.din()
        res = sess.query(Province).all()
        return res


class FranchiseModel(object):
    def add(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def getOne(self):
        pass

    def fetchAll(self):
        sess = self.din()
        res = sess.query(Franchise).all()
        return res