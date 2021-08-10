import os.path
import dbm
from dbm import dumb as dbmdumb
from dbm import ndbm as dbmndbm
AllowGNU = True
try:
    from dbm import gnu as dbmgnu
except:
    AllowGNU = False

_db_type_dict = {
            'dbm.gnu': 0,
            'dbm.ndbm': 1,
            'dbm.dumb': 2,
        }

class DB:
    db = None

    def __init__(self, filename = None, mode = 0):
        if filename:
            self.openf(filename, mode)

    def openf(self, filename, mode = 0):
        exists = [1, 1, 1]
        # gnu
        if not os.path.exists(filename):
            exists[0] = 0
        
        # ndbm
        if not os.path.exists(filename + '.db'):
            exists[1] = 0
    
        # dumb
        if not (os.path.exists(filename + '.dir') and os.path.exists(filename + '.bak') and os.path.exists(filename + '.dir')):
            exists[2] = 0
    
        if any(exists):
            if exists[0]:
                db = dbmgnu.open(filename, 'c')
                self._db_type = 0
            elif exists[1]:
                db = dbmndbm.open(filename, 'c')
                self._db_type = 1
            else:
                db = dbmdumb.open(filename, 'c')
                self._db_type = 2
        else: 
            if mode == 0 and AllowGNU:
                db = dbmgnu.open(filename, 'c')
                self._db_type = 0
            elif mode == 2:
                db = dbmdumb.open(filename, 'c')
                self._db_type = 2
            else:
                db = dbmndbm.open(filename, 'c')
                self._db_type = 1
            #self._db_type = _db_type_dict[dbm.whichdb(filename)]
            if not AllowGNU and mode == 0:
                self._db_type = 1
            else:
                self._db_type = mode
    
        self.filename = filename
        self.__call__(db)

    @staticmethod
    def open(filename):
        return DB(filename)
    
    def allkeys(self):
        db = self.db
        if self._db_type == 0:
            ks = []
            k = db.firstkey()
            while k != None:
                ks.append(k)
                k = db.nextkey(k)
        else:
            ks = db.keys()
        return ks

    def close(db):
        db.db.close()
    
    def sync(self):
        db = self.db
        if self._db_type == 0:
                db.reorganize()
        if self._db_type == 1:
            db.close()
            self.openf(self.filename)
        else:
            db.sync()

    def get(self, key, default = None):
        key = self.tobytes(key)
        if key in self.allkeys():
            return self[key]
        return default

    @staticmethod
    def tobytes(c):
        if isinstance(c, (bytes, bytearray, memoryview)):
            return c
        elif isinstance(c, str):
            return c.encode('utf-8')
        else:
            return str(c).encode('utf-8')

    @property
    def type(self):
        return {v:k for k, v in _db_type_dict.items()}[self._db_type]

    def __call__(self, db):
        self.db = db

    def __getitem__(self, *args, **kwargs):
        db = self.db
        return db.__getitem__(*args, **kwargs)

    def __setitem__(self, *args, **kwargs):
        return self.db.__setitem__(*args, **kwargs)

    def __delitem__(self, *args, **kwargs):
        return self.db.__delitem__(*args, **kwargs)

if __name__ == '__main__':
    db = DB('data', 2)
    print(db.type)
    db['a'] = 'b'
    assert db['a'] == b'b'
    
    db.sync()
    db.close()
else:
    if AllowGNU:
        _fn = 'data.db'
    else:
        _fn = 'data'
    db = DB(_fn)
