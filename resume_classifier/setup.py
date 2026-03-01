#!/usr/bin/env python3
"""
Setup script for AI Resume Classifier
"""

import os
import sys
import subprocess
import shutil

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Error: Python 3.8 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python {sys.version.split()[0]} detected")
    return True

def install_requirements():
    """Install required packages"""
    print("\n📦 Installing requirements...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing requirements: {e}")
        return False

def create_env_file():
    """Create .env file if it doesn't exist"""
    if not os.path.exists('.env'):
        print("\n🔧 Creating .env file...")
        try:
            shutil.copy('env_example.txt', '.env')
            print("✅ .env file created")
            print("⚠️  Please edit .env file and add your OpenAI API key")
            return True
        except FileNotFoundError:
            print("❌ env_example.txt not found")
            return False
    else:
        print("✅ .env file already exists")
        return True

def create_upload_directory():
    """Create uploads directory"""
    uploads_dir = 'uploads'
    if not os.path.exists(uploads_dir):
        os.makedirs(uploads_dir)
        print("✅ Uploads directory created")
    else:
        print("✅ Uploads directory already exists")
    return True

def main():
    """Main setup function"""
    print("🚀 AI Resume Classifier Setup")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        return False
    
    # Install requirements
    if not install_requirements():
        return False
    
    # Create .env file
    if not create_env_file():
        return False
    
    # Create uploads directory
    if not create_upload_directory():
        return False
    
    print("\n" + "=" * 40)
    print("✅ Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Edit .env file and add your OpenAI API key")
    print("2. Run 'python app.py' to start the application")
    print("3. Open http://localhost:5000 in your browser")
    print("\n📖 For more information, see README.md")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 