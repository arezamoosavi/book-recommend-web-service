import logging
from flask import request, Response, json, jsonify
from flask_restful import Resource
from app.Utils.Auth.TokenConfig import Auth
from app.models.user import UserModel

logging.basicConfig(filename='logfiles.log',
                    level=logging.DEBUG,
                    format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")



class signIn(Resource):
    
    def post(self):

        req_data = {}
        req_data['username'] = request.values.get('username', None)
        req_data['password'] = request.values.get('password', None)
        
        print('\nff'*5, req_data, '\n**'*5)

        get_user = UserModel.find_username(_username=req_data['username'])

        if get_user:
            user = get_user.first()
            print(user.is_admin,'**********\n\n')
            if user.check_password(password=req_data['password']):

                token = Auth.generate_token(user.username)
                message = {'Token': token}
                return jsonify(message)
            else:
                message = {'MSG': "wrong password!"}
                return jsonify(message)


        admin = request.values.get('admin', None)

        if admin=='yes':
            new_user = UserModel.create_admin(username=req_data['username'], 
            password=req_data['password'])
        else:
            new_user = UserModel.create_user(username=req_data['username'], 
            password=req_data['password'])
        
        try:
            new_user.save()

        except Exception as e:

            logging.error('Error! {}'.format(e))
            return jsonify({"Error":e})

        print(new_user.items())
        token = Auth.generate_token(new_user.username)

        print('\n\n', token)

        retJson = {
            "jwt_token": token,
            "status": 201,
             }
    
        return jsonify(retJson)
