import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Configuration class for the Weather Prediction App"""
    
    # Flask Configuration
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'weather_prediction_secret_key'
    DEBUG = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    
    # Kaggle API Configuration
    KAGGLE_USERNAME = os.environ.get('KAGGLE_USERNAME')
    KAGGLE_KEY = os.environ.get('KAGGLE_KEY')
    
    # Weather API Configuration
    OPENWEATHER_API_KEY = os.environ.get('OPENWEATHER_API_KEY')
    
    # Model Configuration
    MODEL_PATH = 'models/weather_model.pkl'
    SCALER_PATH = 'models/scaler.pkl'
    
    # Data Configuration
    DATA_CACHE_DIR = 'data_cache'
    MAX_PREDICTION_DAYS = 14
    
    # Logging Configuration
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')
    
    @staticmethod
    def init_app(app):
        """Initialize app with configuration"""
        # Create necessary directories
        os.makedirs('models', exist_ok=True)
        os.makedirs('data_cache', exist_ok=True)
        os.makedirs('templates', exist_ok=True)

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False

class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    DEBUG = True

# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
} 