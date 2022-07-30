from flask import Flask, request
from flask_restful import Resource, Api
import pandas as pd
from marshmallow import Schema, fields


app = Flask(__name__)
api = Api(app)

data = pd.read_csv('healthcare-dataset-stroke-data.csv')

class StrokeSchema(Schema):
    ids = fields.List(fields.Int(), required=True)

stroke_schema = StrokeSchema()

class Stroke(Resource):
    def get(self):
        args = request.args.to_dict()
        if 'ids' in args:
            args['ids'] = args['ids'].split(',')
        errors = stroke_schema.validate(args)

        if len(errors) > 0:
            return {'message': errors}, 404
        
        res = {"id":dict()}
        cols = list(data.columns)[1:]
        
        for id in args['ids']:
            id = int(id)
            val_list = data[data.id==id].values.tolist()
            if len(val_list) == 0:
                res['id'][id] = {'data':{}, 'message':f'Failure - {id} is not valid id!'}
            else:
                vals = val_list[0][1:]
                res['id'][id]= {
                    'data': {
                        cols[i]:vals[i] for i in range(len(cols))
                    }, 'message':'Success!'
                }
        return res, 200

api.add_resource(Stroke, '/stroke')

if __name__ == '__main__':
    app.run(debug=True)
