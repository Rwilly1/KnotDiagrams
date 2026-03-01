# VR Web Local

This is a local clone of the VR Web project for development and testing purposes.

## Project Overview

This Flask web application provides a VR interface for learning how to tie knots. It uses Teachable Machine for real-time webcam detection of knot-tying steps.

## Setup Instructions

1. Create a virtual environment (recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python app.py
   ```

4. Open your browser and navigate to:
   ```
   http://localhost:5001
   ```

## Project Structure

- `app.py` - Main Flask application
- `requirements.txt` - Python dependencies
- `templates/` - HTML templates
- `static/` - Static assets (images, CSS, JS)

## Features

- Step-by-step knot tying instructions with images
- Real-time webcam detection using Teachable Machine
- Interactive navigation between steps

## Development Notes

This is a local development version that is not configured for deployment. You can modify this version freely without affecting the original repository.
