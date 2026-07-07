from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle
import pandas as pd
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

# Load trained model
with open("BigMart_Sales_Model.pkl", "rb") as file:
    model = pickle.load(file)

# Feature columns (must match training columns in order and type)
feature_names = [
    'Item_Weight', 'Item_Fat_Content', 'Item_Visibility', 'Item_MRP',
    'Outlet_Size', 'Outlet_Location_Type', 'Outlet_Type', 'Outlet_Age',
    'Item_Type_Breads', 'Item_Type_Breakfast', 'Item_Type_Canned',
    'Item_Type_Dairy', 'Item_Type_Frozen Foods',
    'Item_Type_Fruits and Vegetables', 'Item_Type_Hard Drinks',
    'Item_Type_Health and Hygiene', 'Item_Type_Household', 'Item_Type_Meat',
    'Item_Type_Others', 'Item_Type_Seafood', 'Item_Type_Snack Foods',
    'Item_Type_Soft Drinks', 'Item_Type_Starchy Foods',
    'Item_Identifier_Categories_FD', 'Item_Identifier_Categories_NC',
    'Outlet_Identifier_OUT013', 'Outlet_Identifier_OUT017',
    'Outlet_Identifier_OUT018', 'Outlet_Identifier_OUT019',
    'Outlet_Identifier_OUT027', 'Outlet_Identifier_OUT035',
    'Outlet_Identifier_OUT045', 'Outlet_Identifier_OUT046',
    'Outlet_Identifier_OUT049'
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict')
def predict_page():
    return render_template('predict.html')

@app.route('/predict_sales', methods=['POST'])
def predict_sales():
    try:
        data = request.get_json()
        
        # Extract features from request
        features = []
        
        # Numeric features
        features.extend([
            float(data['item_weight']),
            int(data['item_fat_content']),
            float(data['item_visibility']),
            float(data['item_mrp']),
            int(data['outlet_size']),
            int(data['outlet_location_type']),
            int(data['outlet_type']),
            float(data['outlet_age'])
        ])
        
        # Binary item type features
        item_types = [
            'item_type_breads', 'item_type_breakfast', 'item_type_canned',
            'item_type_dairy', 'item_type_frozen_foods', 'item_type_fruits_vegetables',
            'item_type_hard_drinks', 'item_type_health_hygiene', 'item_type_household',
            'item_type_meat', 'item_type_others', 'item_type_seafood',
            'item_type_snack_foods', 'item_type_soft_drinks', 'item_type_starchy_foods'
        ]
        
        for item_type in item_types:
            features.append(1 if data.get(item_type, False) else 0)
        
        # Binary identifier features
        identifiers = [
            'item_identifier_fd', 'item_identifier_nc',
            'outlet_identifier_out013', 'outlet_identifier_out017',
            'outlet_identifier_out018', 'outlet_identifier_out019',
            'outlet_identifier_out027', 'outlet_identifier_out035',
            'outlet_identifier_out045', 'outlet_identifier_out046',
            'outlet_identifier_out049'
        ]
        
        for identifier in identifiers:
            features.append(1 if data.get(identifier, False) else 0)
        
        # Convert to DataFrame and predict
        input_array = np.array(features).reshape(1, -1)
        input_df = pd.DataFrame(input_array, columns=feature_names)
        
        prediction = model.predict(input_df)[0]
        
        return jsonify({
            'success': True,
            'prediction': f"₹{prediction:.2f}",
            'prediction_value': prediction
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 
