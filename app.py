from flask import Flask, render_template, request, jsonify
import uuid
from datetime import datetime, timedelta

app = Flask(__name__)

# In-memory session storage (for development - use Redis/database in production)
sessions = {}

# Clean up old sessions (older than 24 hours)
def cleanup_sessions():
    current_time = datetime.now()
    expired = [sid for sid, data in sessions.items() 
               if current_time - data.get('last_updated', current_time) > timedelta(hours=24)]
    for sid in expired:
        del sessions[sid]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/session/create', methods=['POST'])
def create_session():
    cleanup_sessions()
    import random
    session_id = str(random.randint(1000, 9999))  # 4-digit session ID
    sessions[session_id] = {
        'current_step': 1,
        'current_knot': 'single',
        'last_updated': datetime.now()
    }
    return jsonify({'session_id': session_id})

@app.route('/api/session/<session_id>/state', methods=['GET'])
def get_state(session_id):
    if session_id not in sessions:
        return jsonify({'error': 'Session not found'}), 404
    return jsonify(sessions[session_id])

@app.route('/api/session/<session_id>/state', methods=['POST'])
def update_state(session_id):
    if session_id not in sessions:
        return jsonify({'error': 'Session not found'}), 404
    
    data = request.json
    sessions[session_id].update({
        'current_step': data.get('current_step', sessions[session_id]['current_step']),
        'current_knot': data.get('current_knot', sessions[session_id]['current_knot']),
        'last_updated': datetime.now()
    })
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
