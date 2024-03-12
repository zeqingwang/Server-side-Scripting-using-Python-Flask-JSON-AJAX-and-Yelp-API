import requests

from unicodedata import category
from flask import Flask
from flask import request
from flask import jsonify

import json
app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('page1.html')
    #return render_template("page1.html")
@app.route('/search', methods=['get'])

def search():
    request_dict=request.args.to_dict()
    term=request_dict["keyword"]
    latitude=request_dict["latitude"]
    longitude=request_dict["longitude"]
    radius=int(float(request_dict["distance"])*1609.344)
    category=request_dict["category"]


    yelp_link="https://api.yelp.com/v3/businesses/search?"
    yelp_link+="term="+term
    yelp_link+="&latitude="+latitude
    yelp_link+="&longitude="+longitude
    yelp_link+="&radius="+str(radius)
    yelp_link+="&categories="+category
    yelp_key="1a7B6MgzsBffRHrMceajNfbBTWinuOTaUHIQRbi4EFKTwMHgCdwZAxYHqQ8Cghj6QAwRR2txjbmORWhlEAB5RJh11n2rUEVKqcDTQG-m99dOpJUQCy9oyiISAQs5Y3Yx"
    
    print("111"+yelp_link)
    headers={'Authorization':'Bearer %s'%yelp_key}
    response=requests.get(url=yelp_link,headers=headers).json()
    #print(json.dumps(response))
    #print(response["businesses"][0])
    #return jsonify(response)
    #print(jsonify(response))
    #yelp_result=json.load({})
    content=[]
    result_num=response["total"]
    return_num=20
    if result_num<20:
        return_num=result_num
    #print(return_num)  
    #print(response["businesses"][19])
    for i in range(return_num):
        content.append(response["businesses"][i])
    result_dict={"number":return_num,"data":content}
    return_json=jsonify(result_dict)
    return_json.headers['Access-Control-Allow-Origin'] = '*'

    #print(result_dict)
    return return_json
@app.route('/detail', methods=['get'])

def detail():
    request_id=request.args.to_dict()["id"]

    print(request_id)
    detaillink="https://api.yelp.com/v3/businesses/"
    detaillink+=request_id
    
    yelp_key="1a7B6MgzsBffRHrMceajNfbBTWinuOTaUHIQRbi4EFKTwMHgCdwZAxYHqQ8Cghj6QAwRR2txjbmORWhlEAB5RJh11n2rUEVKqcDTQG-m99dOpJUQCy9oyiISAQs5Y3Yx"
    headers={'Authorization':'Bearer %s'%yelp_key}
    detail_response=requests.get(url=detaillink,headers=headers).json()
    print(detail_response)
    content=[]
    content.append(detail_response)
    detail_dict={"data":detail_response}
    detail_json=jsonify(detail_dict)
    detail_json.headers['Access-Control-Allow-Origin'] = '*'



    return detail_json


    

    
    

if __name__ == '__main__':
    app.run(debug=True)