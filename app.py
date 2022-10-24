import requests
import json 

from flask import Flask, request

app = Flask(__name__)

headers = {
    "X-RapidAPI-Key": "eb35fcf224msh909175e8c268c99p18336bjsn1e11ec2eeddf",
    "X-RapidAPI-Host": "themealdb.p.rapidapi.com"
}

@app.route('/')
def home():
    return """<h3>Endpoints</h3>
    <p>See <a href=https://rapidapi.com/thecocktaildb/api/themealdb/>The meal DB API Docs</a><p>
    <h4>1. Filter: /filter?<i>param</i>&=<i>arg</i></h4>
    <p>params</p>
    <ul>
        <li>i: ingredient(s). eg <a href=/filter?i&=chicken_breast>/filter?i&=chicken_breast</a></li>
        <li>c: category. eg <a href=/filter?c&=seafood>/filter?c&=seafood</a></li>
        <li>a: area. eg <a href=/filter?a&=Canadian>/filter?a&=Canadian</a></li>
    </ul>
    <p></p>

    <h4>2. Search: /search?<i>param</i>&=<i>arg</i></h4>
    <p>params<p>
        <ul>
        <li>s: search by name. eg <a href=/search?s&=Arrabiata>/search?s&=Arrabiata</a></li>
        <li>f: search by first letter. eg <a href=/search?s&=a>/search?s&=a</a></li>
    </ul>

    <h4>3. Lookup: /lookup?<i>param</i>&=<i>arg</i></h4>
    <p>params<p>
    <ul>
        <li>r: random recipe (no arg). eg <a href=/lookup?r>/lookup?r</a></li>
        <li>t: random 10 recipes (no arg). eg <a href=/lookup?t>/lookup?t</a></li>
        <li>i: lookup by id. eg <a href=/lookup?i&=52772>/lookup?i&=52772</a></li>
    </ul>

    <h4>4. List /list?<i>param</i>&=<i>arg</i></h4>
    <p>params<p>
    </ul>
        <li>i: list all recipe  Ingredients. eg <a href=/list?i>/list?i</a></li>
        <li>a: list all recipe areas. eg <a href=/list?a&=list>/list?a&=list</a></li>
        <li>c: list all recipe  category. eg <a href=/list?c&=list>/list?c&=list</a></li>
        <li>l: list all meal categories (no arg). eg <a href=/list?l>/list?l</a></li>
        <li>m: latest meal (no arg). eg <a href=/list?m>/list?m</a></li>
    """

     

@app.route('/filter')
def filter():
    key_str = 'c'
    value_str = 'seafood'
    for key, value in request.args.lists():
        key_str = key if key != "" else key_str
        value_str = value if value != "" else value_str

    querystring = {key_str: value_str}
    
    response = requests.request("GET", "https://themealdb.p.rapidapi.com/filter.php", 
                                headers=headers, params=querystring)

    #print(json.dumps(response.json(), indent=2))
    return response.json()

@app.route('/search')
def search():
    key_str = 'f'
    value_str = 'a'
    for key, value in request.args.lists():
        key_str = key if key != "" else key_str
        value_str = value if value != "" else value_str

    querystring = {key_str: value_str}
    
    response = requests.request("GET", "https://themealdb.p.rapidapi.com/search.php", 
                                headers=headers, params=querystring)

    #print(json.dumps(response.json(), indent=2))
    return response.json()

@app.route('/lookup')
def lookup():
    key_str = 'f'
    value_str = 'a'
    for key, value in request.args.lists():
        key_str = key if key != "" else key_str
        value_str = value if value != "" else value_str

    if key_str == 'r':
        response = requests.request("GET", "https://themealdb.p.rapidapi.com/random.php", headers=headers)
    elif key_str == 't':
        response = requests.request("GET", "https://themealdb.p.rapidapi.com/randomselection.php", headers=headers)
    else:
        querystring = {key_str: value_str}
    
        response = requests.request("GET", "https://themealdb.p.rapidapi.com/lookup.php", 
                                    headers=headers, params=querystring)

    #print(json.dumps(response.json(), indent=2))
    return response.json()

@app.route('/list')
def list():
    key_str = 'f'
    value_str = 'a'
    for key, value in request.args.lists():
        key_str = key if key != "" else key_str
        value_str = value if value != "" else value_str

    if key_str == 'l':
        response = requests.request("GET", "https://themealdb.p.rapidapi.com/categories.php", headers=headers)
    elif key_str == 'm':
        response = requests.request("GET", "https://themealdb.p.rapidapi.com/latest.php", headers=headers)
    else:
        querystring = {key_str: value_str}
        response = requests.request("GET", "https://themealdb.p.rapidapi.com/list.php", 
                                headers=headers, params=querystring)

    #print(json.dumps(response.json(), indent=2))
    return response.json()