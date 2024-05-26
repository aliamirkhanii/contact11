from flask import Flask, request
from flask_restful import Api, Resource
from test1.Schemaa import MySchema
import json

app = Flask(__name__)
api = Api(app)
# file that save
file_path = "data.json"
schema = MySchema()


class Contact(Resource):
    # read data and load from file and use GET method
    @staticmethod
    def get():
        try:
            with open(file_path, 'r') as jf:
                data = json.load(jf)
            return data, 200
        except Exception as e:
            print(e)
            return f'Something Went Wrong: >{e}', 500

    # create a new contact and use POST method
    @staticmethod
    def post():
        try:
            data = schema.load(request.get_json())
            if not (data.get('name') and data.get('phone_number')):
                return {'message': 'pls insert and complete all cell'}, 400
            else:
                name = data.get('name')
                phone = data.get('phone_number')
                with open(file_path, 'r') as f:
                    file = f.read()
                contact = json.dumps(file)
                for num, ph in enumerate(phone):
                    name.update({num: ph})

                # 'a' open for writing, appending to the end of file if it exists
                with open(file_path, 'w') as f:
                    json.dump(contact, f, indent=3)
                return {'message': 'new contact add successfully'}, 201
        except Exception as e:
            print(e)
            return f'Something Went Wrong: >{e}', 500

    # for UPDATE and use PUT method
    @staticmethod
    def put():
        try:
            # first load data and read 'r'
            with open(file_path, 'r') as f_p:
                old_data = json.load(f_p)
            # load new data from request and use schema
            new_data = schema.load(request.get_json())
            # update
            old_data.update(new_data)
            # now save update in file
            # 'w' : overwrite
            with open(file_path, 'w') as f_p:
                json.dump(old_data, f_p, indent=3)
            return {'message': 'phonenumber update'}, 200
        except Exception as e:
            print(e)
            return f'Something Went Wrong: >{e}', 500

    # delete and use DELETE method
    @staticmethod
    def delete():
        try:
            # use {} for replace by f_p
            with open(file_path, 'w') as f_p:
                json.dump({}, f_p, indent=3)
            return {'message': 'delete contact successfully '}
        except Exception as e:
            print(e)
            return f'Something Went Wrong: >{e}', 500


api.add_resource(Contact, '/contact', endpoint='contact')

if __name__ == '__main__':
    app.run(debug=True)
