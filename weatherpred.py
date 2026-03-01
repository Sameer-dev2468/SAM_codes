import os
import json
import requests
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from flask import Flask, render_template, request, jsonify
import plotly.graph_objs as go
import plotly.utils
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import warnings
warnings.filterwarnings('ignore')


app = Flask(__name__)
app.secret_key = 'weather_prediction_secret_key'


weather_model = None
scaler = None
is_model_trained = False

class WeatherPredictor:
    def __init__(self):
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.scaler = StandardScaler()
        self.is_trained = False
        
    def fetch_kaggle_weather_data(self, location):
        """
        Fetch weather data from Kaggle API
        Note: You'll need to set up Kaggle API credentials
        """
        try:
          
            return self.generate_sample_data(location)
        except Exception as e:
            print(f"Error fetching Kaggle data: {e}")
            return self.generate_sample_data(location)
    
    def generate_sample_data(self, location):
        """Generate sample weather data for demonstration"""
        dates = pd.date_range(start='2020-01-01', end='2024-01-01', freq='D')
        
        
        np.random.seed(42)
        base_temp = 20 + 10 * np.sin(2 * np.pi * dates.dayofyear / 365)
        temperature = base_temp + np.random.normal(0, 5, len(dates))
        
        humidity = 60 + 20 * np.sin(2 * np.pi * dates.dayofyear / 365) + np.random.normal(0, 10, len(dates))
        humidity = np.clip(humidity, 0, 100)
        
        pressure = 1013 + np.random.normal(0, 10, len(dates))
        wind_speed = np.random.exponential(5, len(dates))
        
       
        conditions = ['Sunny', 'Cloudy', 'Rainy', 'Partly Cloudy', 'Stormy']
        weather_condition = np.random.choice(conditions, len(dates), p=[0.4, 0.3, 0.2, 0.08, 0.02])
        
        data = {
            'date': dates,
            'temperature': temperature,
            'humidity': humidity,
            'pressure': pressure,
            'wind_speed': wind_speed,
            'weather_condition': weather_condition,
            'location': location
        }
        
        return pd.DataFrame(data)
    
    def prepare_features(self, df):
        """Prepare features for machine learning"""
        df['date'] = pd.to_datetime(df['date'])
        df['day_of_year'] = df['date'].dt.dayofyear
        df['month'] = df['date'].dt.month
        df['day_of_week'] = df['date'].dt.dayofweek
        
        
        df['temp_lag1'] = df['temperature'].shift(1)
        df['temp_lag2'] = df['temperature'].shift(2)
        df['temp_lag7'] = df['temperature'].shift(7)
        
        
        df['temp_rolling_7'] = df['temperature'].rolling(window=7).mean()
        df['humidity_rolling_7'] = df['humidity'].rolling(window=7).mean()
        
        # Drop NaN values
        df = df.dropna()
        
        return df
    
    def train_model(self, location):
        """Train the weather prediction model"""
        print(f"Fetching data for {location}...")
        df = self.fetch_kaggle_weather_data(location)
        df = self.prepare_features(df)
        
       
        feature_columns = [
            'day_of_year', 'month', 'day_of_week',
            'temp_lag1', 'temp_lag2', 'temp_lag7',
            'temp_rolling_7', 'humidity_rolling_7',
            'humidity', 'pressure', 'wind_speed'
        ]
        
        X = df[feature_columns]
        y_temp = df['temperature']
        y_humidity = df['humidity']
        
        
        X_train, X_test, y_train_temp, y_test_temp = train_test_split(
            X, y_temp, test_size=0.2, random_state=42
        )
        

        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        
        self.model.fit(X_train_scaled, y_train_temp)
        
        
        y_pred = self.model.predict(X_test_scaled)
        mse = mean_squared_error(y_test_temp, y_pred)
        r2 = r2_score(y_test_temp, y_pred)
        
        self.is_trained = True
        
        return {
            'mse': mse,
            'r2': r2,
            'feature_importance': dict(zip(feature_columns, self.model.feature_importances_))
        }
    
    def predict_weather(self, location, days_ahead=7):
        """Predict weather for the next N days"""
        if not self.is_trained:
            self.train_model(location)

        
        df = self.fetch_kaggle_weather_data(location)
        df = self.prepare_features(df)
        
        
        last_date = df['date'].max()
        future_dates = pd.date_range(start=last_date + timedelta(days=1), periods=days_ahead, freq='D')
        
        predictions = []
        
        for i, future_date in enumerate(future_dates):
           
            features = {
                'day_of_year': future_date.dayofyear,
                'month': future_date.month,
                'day_of_week': future_date.dayofweek,
                'temp_lag1': df['temperature'].iloc[-1] if i == 0 else predictions[-1]['temperature'],
                'temp_lag2': df['temperature'].iloc[-2] if i < 2 else predictions[-2]['temperature'],
                'temp_lag7': df['temperature'].iloc[-7] if i < 7 else predictions[-7]['temperature'],
                'temp_rolling_7': df['temperature'].tail(7).mean(),
                'humidity_rolling_7': df['humidity'].tail(7).mean(),
                'humidity': df['humidity'].iloc[-1],
                'pressure': df['pressure'].iloc[-1],
                'wind_speed': df['wind_speed'].iloc[-1]
            }
            
            feature_vector = np.array([[
                features['day_of_year'], features['month'], features['day_of_week'],
                features['temp_lag1'], features['temp_lag2'], features['temp_lag7'],
                features['temp_rolling_7'], features['humidity_rolling_7'],
                features['humidity'], features['pressure'], features['wind_speed']
            ]])
            
            
            feature_vector_scaled = self.scaler.transform(feature_vector)
            
            
            predicted_temp = self.model.predict(feature_vector_scaled)[0]
            
           
            predicted_humidity = max(0, min(100, 80 - predicted_temp * 0.5 + np.random.normal(0, 5)))
            
            
            if predicted_temp > 25 and predicted_humidity < 60:
                condition = 'Sunny'
            elif predicted_temp < 10:
                condition = 'Cold'
            elif predicted_humidity > 80:
                condition = 'Rainy'
            else:
                condition = 'Partly Cloudy'
            
            predictions.append({
                'date': future_date.strftime('%Y-%m-%d'),
                'temperature': round(predicted_temp, 1),
                'humidity': round(predicted_humidity, 1),
                'condition': condition,
                'pressure': round(features['pressure'] + np.random.normal(0, 2), 1),
                'wind_speed': round(features['wind_speed'] + np.random.normal(0, 1), 1)
            })
        
        return predictions


weather_predictor = WeatherPredictor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        location = data.get('location', 'New York')
        days_ahead = int(data.get('days_ahead', 7))
        
        
        if not weather_predictor.is_trained:
            training_results = weather_predictor.train_model(location)
        
        
        predictions = weather_predictor.predict_weather(location, days_ahead)
        
        
        dates = [p['date'] for p in predictions]
        temperatures = [p['temperature'] for p in predictions]
        humidity = [p['humidity'] for p in predictions]
        
       
        temp_fig = go.Figure()
        temp_fig.add_trace(go.Scatter(
            x=dates, y=temperatures,
            mode='lines+markers',
            name='Temperature (°C)',
            line=dict(color='red', width=3),
            marker=dict(size=8)
        ))
        temp_fig.update_layout(
            title=f'Temperature Forecast for {location}',
            xaxis_title='Date',
            yaxis_title='Temperature (°C)',
            template='plotly_white'
        )
        
         
        hum_fig = go.Figure()
        hum_fig.add_trace(go.Scatter(
            x=dates, y=humidity,
            mode='lines+markers',
            name='Humidity (%)',
            line=dict(color='blue', width=3),
            marker=dict(size=8)
        ))
        hum_fig.update_layout(
            title=f'Humidity Forecast for {location}',
            xaxis_title='Date',
            yaxis_title='Humidity (%)',
            template='plotly_white'
        )
        
        return jsonify({
            'success': True,
            'predictions': predictions,
            'temperature_plot': json.dumps(temp_fig, cls=plotly.utils.PlotlyJSONEncoder),
            'humidity_plot': json.dumps(hum_fig, cls=plotly.utils.PlotlyJSONEncoder),
            'location': location
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/train', methods=['POST'])
def train_model():
    try:
        data = request.get_json()
        location = data.get('location', 'New York')
        
        results = weather_predictor.train_model(location)
        
        return jsonify({
            'success': True,
            'results': results,
            'message': f'Model trained successfully for {location}'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
