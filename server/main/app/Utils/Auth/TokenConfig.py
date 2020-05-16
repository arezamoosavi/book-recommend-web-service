import datetime
import os
from functools import wraps

import jwt
from flask import Response, json, request, g

from app.models.user import UserModel


class Auth():
    @staticmethod
    def generate_token(username):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
                'iat': datetime.datetime.utcnow(),
                'sub': username
            }
            return jwt.encode(payload, os.getenv('JWT_SECRET_KEY'), 'HS256').decode('utf-8')

        except Exception as e:
            return Response(
                mimetype='application/type',
                response=json.dumps({'error': 'Error in generating user token.'}),
                status=400
            )

    @staticmethod
    def decode_token(token):
        re = {'data': {}, 'error': {}}
        try:
            payload = jwt.decode(token, os.getenv('JWT_SECRET_KEY'))
            re['data'] = {'username': payload['sub']}
            return re
        except jwt.ExpiredSignatureError as e1:
            re['error'] = {'message': 'Tokon expired.'}
            return re
        except jwt.InvalidTokenError as e2:
            re['error'] = {'message': 'Invalid token'}
            return re

    @staticmethod
    def auth_required(func):
        @wraps(func)
        def decorated_auth(*args, **kwargs):
            if 'api-token' not in request.headers:
                return Response(
                    mimetype='application/json',
                    response=json.dumps({'error': 'Authentication token is not available.'}),
                    status=400
                )
            token = request.headers.get('api-token')
            data = Auth.decode_token(token)
            if data['error']:
                return Response(
                    mimetype='application/json',
                    response=json.dumps(data['error']),
                    status=400
                )

            username = data['data']['username']
            user = UserModel.find_username(_username=username)
            if not user:
                return Response(
                    mimetype='application/json',
                    response=json.dumps({'error': 'User does not exist.'}, ),
                    status=400
                )
            return func(*args, **kwargs)

        return decorated_auth

    @staticmethod
    def auth_admin(func):
        @wraps(func)
        def decorated_auth(*args, **kwargs):
            if 'api-token' not in request.headers:
                return Response(
                    mimetype='application/json',
                    response=json.dumps({'error': 'Authentication token is not available.'}),
                    status=400
                )
            token = request.headers.get('api-token')
            data = Auth.decode_token(token)
            if data['error']:
                return Response(
                    mimetype='application/json',
                    response=json.dumps(data['error']),
                    status=400
                )

            username = data['data']['username']
            user = UserModel.find_username(_username=username)
            if not user:
                return Response(
                    mimetype='application/json',
                    response=json.dumps({'error': 'User does not exist.'}, ),
                    status=400
                )
            elif not user.first().is_admin:
                return Response(
                    mimetype='application/json',
                    response=json.dumps({'error': 'Only Admin!.'}, ),
                    status=400
                )

            return func(*args, **kwargs)

        return decorated_auth
