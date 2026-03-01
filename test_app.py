#!/usr/bin/env python3
"""
Test script for the Weather Prediction Application
"""

import sys
import os
import requests
import json
from weatherpred import app, weather_predictor

def test_model_training():
    """Test the model training functionality"""
    print("Testing model training...")
    try:
        results = weather_predictor.train_model("New York")
        print(f"✅ Model training successful!")
        print(f"   MSE: {results['mse']:.4f}")
        print(f"   R² Score: {results['r2']:.4f}")
        return True
    except Exception as e:
        print(f"❌ Model training failed: {e}")
        return False

def test_weather_prediction():
    """Test the weather prediction functionality"""
    print("Testing weather prediction...")
    try:
        predictions = weather_predictor.predict_weather("New York", 7)
        print(f"✅ Weather prediction successful!")
        print(f"   Generated {len(predictions)} predictions")
        
        # Print first prediction
        if predictions:
            first_pred = predictions[0]
            print(f"   Sample prediction: {first_pred['date']} - {first_pred['temperature']}°C, {first_pred['condition']}")
        
        return True
    except Exception as e:
        print(f"❌ Weather prediction failed: {e}")
        return False

def test_flask_app():
    """Test the Flask application"""
    print("Testing Flask application...")
    try:
        with app.test_client() as client:
            # Test main page
            response = client.get('/')
            if response.status_code == 200:
                print("✅ Main page loads successfully")
            else:
                print(f"❌ Main page failed: {response.status_code}")
                return False
            
            # Test prediction endpoint
            response = client.post('/predict', 
                                json={'location': 'New York', 'days_ahead': 3})
            if response.status_code == 200:
                data = json.loads(response.data)
                if data.get('success'):
                    print("✅ Prediction endpoint works")
                else:
                    print(f"❌ Prediction failed: {data.get('error')}")
                    return False
            else:
                print(f"❌ Prediction endpoint failed: {response.status_code}")
                return False
        
        return True
    except Exception as e:
        print(f"❌ Flask app test failed: {e}")
        return False

def test_dependencies():
    """Test if all required dependencies are available"""
    print("Testing dependencies...")
    required_packages = [
        'flask', 'pandas', 'numpy', 'sklearn', 
        'plotly', 'requests', 'joblib'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} - MISSING")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n❌ Missing packages: {', '.join(missing_packages)}")
        print("Please install missing packages with: pip install -r requirements.txt")
        return False
    
    print("✅ All dependencies available")
    return True

def main():
    """Run all tests"""
    print("=" * 50)
    print("Weather Prediction App - Test Suite")
    print("=" * 50)
    
    tests = [
        ("Dependencies", test_dependencies),
        ("Model Training", test_model_training),
        ("Weather Prediction", test_weather_prediction),
        ("Flask Application", test_flask_app)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n{test_name}:")
        if test_func():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The application is ready to run.")
        print("\nTo start the application, run:")
        print("python weatherpred.py")
        print("\nThen open your browser to: http://localhost:5000")
    else:
        print("❌ Some tests failed. Please check the errors above.")
        sys.exit(1)

if __name__ == "__main__":
    main() 