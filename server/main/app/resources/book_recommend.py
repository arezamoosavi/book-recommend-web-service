import logging
from flask_restful import Resource
from flask import jsonify, request, json, make_response
from app.Utils.recUtils.RecEngine import recBooks
#loging
logging.basicConfig(filename='logfiles.log',
                    level=logging.DEBUG,
                    format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")


class Recommend(Resource):
    
    def get(self,book: str, number:int=6):

        books, called = recBooks(book=book, k=number)
        # recTask = async_recommend.delay(nook=book, k=number)
        # books, called = recTask.wait(timeout=None, interval=0.5)

        if books:
            rec_success = True
        else:
            rec_success = False


        if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
            ip_address=request.environ['REMOTE_ADDR']
        else:
            ip_address=request.environ['HTTP_X_FORWARDED_FOR'] # if behind a proxy
        
        #agent
        user_agent = request.user_agent.string
        
        retJson = {
            "ip_address": ip_address,
            "status":200,
            "books": books,
            "for": "book: {0}, author: {1}".format(called[0], called[1])
             }
    
        return jsonify(retJson)

# class SearchHistory(Resource):
#     def get(self):
        
#         #get ip address
#         if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
#             ip_address=request.environ['REMOTE_ADDR']
#         else:
#             ip_address=request.environ['HTTP_X_FORWARDED_FOR'] # if behind a proxy

#         search_res = MusicModel.find_by_ip(ip=ip_address)

#         return jsonify({'data': [result.serialized for result in search_res]})