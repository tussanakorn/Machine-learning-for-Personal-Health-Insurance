## google sheet
import geopy.distance as ps
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
sheet = client.open("Chatbot-Insurance-Medicine").sheet1

# web service
from flask import Flask, request, jsonify, make_response
import numpy as np
import joblib
# import pickle

app = Flask(__name__)

# load model
# mod = pickle.load(open('medd.mod', 'rb'))
mod = joblib.load("rf_model.joblib")

def load_data():
    data = sheet.get_all_records()
    listdata = pd.DataFrame(data)
    return listdata

@app.route('/')
def index():
    return 'Hello !'

@app.route('/predict', methods=['GET'])
def predict():
    try:
        Age = float(request.args.get('Age',default=1, type=float))
        Diabetes = float(request.args.get('Diabetes',default=1, type=float))
        BloodPressureProblems = float(request.args.get('BloodPressureProblems',default=1, type=float))
        AnyTransplants = float(request.args.get('AnyTransplants',default=1, type=float))
        AnyChronicDiseases = float(request.args.get('AnyChronicDiseases',default=1, type=float))
        Height = float(request.args.get('Height',default=1, type=float))
        Weight = float(request.args.get('Weight',default=1, type=float))
        KnownAllergies = float(request.args.get('KnownAllergies',default=1, type=float))
        HistoryOfCancerInFamily = float(request.args.get('HistoryOfCancerInFamily',default=1, type=float))
        NumberOfMajorSurgeries = float(request.args.get('NumberOfMajorSurgeries',default=1, type=float))

        res = load_data()
        row = [Age,Diabetes,BloodPressureProblems,AnyTransplants,AnyChronicDiseases,Height,Weight,KnownAllergies,HistoryOfCancerInFamily,NumberOfMajorSurgeries]

        list_inp = np.array(row)
        list_re = list_inp.reshape(1,-1)
        pred1 = mod.predict(list_re.tolist()).tolist()
        pred = ' '.join([str(elem) for elem in pred1])

        Prediction = pred
        row1 = [Age,Diabetes,BloodPressureProblems,AnyTransplants,AnyChronicDiseases,Height,Weight,KnownAllergies,HistoryOfCancerInFamily,NumberOfMajorSurgeries,Prediction]
        index = int(len(res)+2)
        sheet.insert_row(row1, index)

        result = {'result':pred}
        return jsonify(result)
        
    except Exception as e :
        return jsonify({'message' : 'error นะ ลองดูใหม่อีกที'})

if __name__ == '__main__':
    app.run(debug=True)
