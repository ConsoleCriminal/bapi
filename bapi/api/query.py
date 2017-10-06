from bapi.api.core import api
from flask_restplus.resource import Resource
from bapi.core.beancount import beancount

ns = api.namespace('query', description='Operations related to bean-query')

@ns.route('/')
class Query(Resource):
    def get(self):
        types, rows = beancount.runQuery('select position')
        
        res = []
        for row in rows:
            resRow = []
            res.append(resRow)
            for col in row:
                resRow.append(col.to_string())
        return res 