from flask import Flask, request, jsonify, render_template
import logging
logging.basicConfig(filename="assignment_logging.log", level=logging.INFO , filemode='w', format="%(asctime)s %(levelname)s %(message)s")

app = Flask(__name__)

@app.route("/", ) #If I just write backslash (/) it will become my homepage of my app. 
def homepage():
    return render_template("index.html") 

@app.route("/demo", methods = ['POST'])
def items_cost():
    """ This is just a demo function to check if the code actually works by testing it in Postman. """

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
    """ This fun will help us to get the "Total cost of 5 items" after applying the relevant discount depending upon the cost of items. """
    try:
        if(request.method == 'POST'):
            Item1= int(request.form['Item1'])
            Item2= int(request.form['Item2'])
            Item3= int(request.form['Item3'])
            Item4= int(request.form['Item4'])
            Item5= int(request.form['Item5'])
            total_cost = Item1 + Item2 + Item3 + Item4 + Item5
            result = 0
            logging.info("I have successfully taken a cost of 5 items from the user")
            logging.info(f"Item1 cost: {Item1}, Item2 cost: {Item2}, Item3 cost: {Item3}, Item4 cost: {Item4}, Item5 cost: {Item5}")             

        if total_cost <= 1000:
            logging.info("I'm inside my 1st discount parameter")
            discount = (total_cost*0.1)
            result = total_cost-discount
            logging.info(f"Total cost after the discount is {result}")

        elif total_cost > 1000 and total_cost <= 2000:
            logging.info("I'm inside my 2st discount parameter")
            discount = (total_cost*0.2)
            result = total_cost-discount
            logging.info(f"Total cost after the discount is {result}")
            
        else:
            logging.info("I'm inside my 3rd discount parameter")
            discount = (total_cost*0.3)
            result = total_cost-discount
            logging.info(f"Total cost after the discount is {result}")
        
        return render_template("result.html", result=result)
        logging.info("Output has been generated successfully")

        
    except Exception as e:
        print("Input/Inputs have been entered incorrectly. Please check and try again.")
        logging.error(e)


if __name__=="__main__":
    app.run(host="0.0.0.0", port=5002)
