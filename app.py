from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/", ) #If I just write backslash (/) it will become my homepage of my app. 
def homepage():
    return render_template("index.html") 

@app.route("/demo", methods = ['POST'])
def items_cost():
    if(request.method == 'POST'):
        Item1= int(request.json['Item1'])
        Item2= int(request.json['Item2'])
        Item3= int(request.json['Item3'])
        Item4= int(request.json['Item4'])
        Item5= int(request.json['Item5'])
        total_cost = Item1 + Item2 + Item3 + Item4 + Item5
        value_after_discount = 0

    if total_cost <= 1000:
        discount = (total_cost*0.1)
        value_after_discount = total_cost-discount

    elif total_cost > 1000 and total_cost <= 2000:
        discount = (total_cost*0.2)
        value_after_discount = total_cost-discount
        
    else:
        discount = (total_cost*0.3)
        value_after_discount = total_cost-discount
    
    return jsonify((f"Your total cost is {total_cost} and value after the discount is {value_after_discount}"))


@app.route("/operation", methods = ['POST'])
def itemscost():
    if(request.method == 'POST'):
        operation = request.form['operation']
        Item1= int(request.form['Item1'])
        Item2= int(request.form['Item2'])
        Item3= int(request.form['Item3'])
        Item4= int(request.form['Item4'])
        Item5= int(request.form['Item5'])
        total_cost = Item1 + Item2 + Item3 + Item4 + Item5
        result = 0

    if total_cost <= 1000:
        discount = (total_cost*0.1)
        result = total_cost-discount

    elif total_cost > 1000 and total_cost <= 2000:
        discount = (total_cost*0.2)
        result = total_cost-discount
        
    else:
        discount = (total_cost*0.3)
        result = total_cost-discount
    
    return render_template ("result.html", result=result)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5001)
