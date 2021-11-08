from flask import Flask ,render_template , request

import pickle

app = Flask(__name__)
#car = pd.read_csv("car_data.csv")
model=pickle.load(open('random_forest_regression_model.pkl','rb'))

@app.route("/",methods=['GET'])
def home():
    return render_template('home.html')



@app.route("/about",methods=['GET'])
def About():
    return render_template('About.html')


@app.route("/contact",methods=['GET'])
def contact():
    return render_template('contact.html')

@app.route("/car_sell",methods=['GET'])
def car_sell():
    return render_template('index2.html')



@app.route("/predict",methods=['POST'])
def predict():
    Fuel_Type_Diesel=0  
    if request.method == 'POST':
        Present_Price=float(request.form['Present_Price'])
        Kms_Driven = int(request.form['Kms_Driven'])
        Owner = int(request.form['Owner'])
        Old_Car = int (request.form['Old_Car'])
        Price_rate_change =  float(request.form['Price_rate_change'])
        Fuel_Type_Petrol = request.form['Fuel_Type_Petrol']
        Fuel_Type_Petrol=request.form['Fuel_Type_Petrol']
        if(Fuel_Type_Petrol=='Petrol'):
            Fuel_Type_Petrol=1
            Fuel_Type_Diesel=0
        else:

            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=1    
        
        Seller_Type_Individual=request.form['Seller_Type_Individual']
        if(Seller_Type_Individual=='Individual'):
            Seller_Type_Individual=1
        else:
            Seller_Type_Individual=0
        Transmission_Manual=request.form['Transmission_Manual']
        if(Transmission_Manual=='Mannual'):
            Transmission_Manual=1
        else:
            Transmission_Manual=0
        
        prediction=model.predict([[Present_Price,Kms_Driven,Owner,Old_Car,Price_rate_change,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Manual]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index2.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index2.html',prediction_text="You Can Sell your Car at {}".format(output))
    else:
        return render_template('index2.html')


  
            

if __name__=='__main__':
    app.run(debug=True)