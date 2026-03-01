# Weather Prediction Web Application

A comprehensive weather prediction web application that uses machine learning to forecast weather conditions based on historical data. The application features a beautiful, modern UI and integrates with Kaggle APIs for data retrieval.

## Features

- 🌤️ **Weather Forecasting**: Predict temperature, humidity, pressure, and wind speed
- 🎯 **Machine Learning**: Uses Random Forest algorithm for accurate predictions
- 📊 **Interactive Visualizations**: Beautiful charts using Plotly
- 🎨 **Modern UI**: Responsive design with gradient backgrounds and smooth animations
- 📱 **Mobile Friendly**: Works perfectly on all devices
- 🔄 **Real-time Predictions**: Get forecasts for 3-14 days ahead
- 📍 **Location-based**: Enter any city name for location-specific forecasts

## Technologies Used

- **Backend**: Flask (Python)
- **Machine Learning**: Scikit-learn (Random Forest)
- **Data Processing**: Pandas, NumPy
- **Visualization**: Plotly
- **Frontend**: HTML5, CSS3, JavaScript
- **Data Source**: Kaggle API (with sample data fallback)

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. **Clone or download the project files**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Kaggle API (Optional)**:
   - Go to [Kaggle](https://www.kaggle.com/) and create an account
   - Go to your account settings and create an API token
   - Download the `kaggle.json` file
   - Place it in `~/.kaggle/kaggle.json` (Linux/Mac) or `C:\Users\<username>\.kaggle\kaggle.json` (Windows)

4. **Run the application**:
   ```bash
   python weatherpred.py
   ```

5. **Open your browser** and go to `http://localhost:5000`

## Usage

1. **Enter Location**: Type a city name (e.g., "New York", "London", "Tokyo")
2. **Select Days**: Choose how many days ahead to predict (3-14 days)
3. **Click Predict**: The application will train the model and generate forecasts
4. **View Results**: See detailed weather cards and interactive charts

## Project Structure

```
weatherpred.py          # Main Flask application
templates/
  index.html           # Web interface
requirements.txt       # Python dependencies
README.md             # This file
```

## How It Works

### Data Processing
- Fetches historical weather data (currently uses sample data)
- Prepares features including:
  - Temporal features (day of year, month, day of week)
  - Lag features (previous day temperatures)
  - Rolling averages
  - Current weather parameters

### Machine Learning Model
- **Algorithm**: Random Forest Regressor
- **Features**: 11 engineered features
- **Target**: Temperature prediction
- **Evaluation**: MSE and R² score

### Prediction Process
1. Train model on historical data
2. Generate feature vectors for future dates
3. Predict temperature using trained model
4. Derive other weather parameters (humidity, pressure, wind)
5. Determine weather conditions based on predictions

## API Endpoints

- `GET /`: Main web interface
- `POST /predict`: Generate weather predictions
- `POST /train`: Train the model for a specific location

## Customization

### Adding Real Kaggle Data
To use real Kaggle weather datasets:

1. Install the kaggle package: `pip install kaggle`
2. Set up your Kaggle API credentials
3. Modify the `fetch_kaggle_weather_data()` method in `weatherpred.py`
4. Replace the sample data generation with actual API calls

### Model Improvements
- Add more weather parameters (precipitation, UV index, etc.)
- Implement ensemble methods
- Add seasonal decomposition
- Include more sophisticated feature engineering

## Troubleshooting

### Common Issues

1. **Port already in use**:
   ```bash
   # Change port in weatherpred.py
   app.run(debug=True, host='0.0.0.0', port=5001)
   ```

2. **Missing dependencies**:
   ```bash
   pip install --upgrade -r requirements.txt
   ```

3. **Kaggle API errors**: The app will fall back to sample data if Kaggle API is not configured

## Future Enhancements

- [ ] Real-time weather API integration
- [ ] Multiple ML algorithms comparison
- [ ] Weather alerts and notifications
- [ ] Historical weather data visualization
- [ ] User accounts and saved locations
- [ ] Mobile app version
- [ ] Advanced weather parameters (snow, fog, etc.)

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Kaggle for providing weather datasets
- Scikit-learn for machine learning capabilities
- Plotly for interactive visualizations
- Flask for the web framework 