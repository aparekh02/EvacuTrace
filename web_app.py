"""
Simple Web UI for EvacuTrace Rescue Simulation
"""

from flask import Flask, render_template, request, jsonify, Response
import subprocess
import threading
import queue
import time
import os

app = Flask(__name__)

# Queue for simulation logs
log_queue = queue.Queue()
simulation_running = False

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/api/upload', methods=['POST'])
def upload_video():
    """Fake video upload endpoint"""
    time.sleep(2)  # Simulate upload time
    return jsonify({
        'status': 'success',
        'message': 'Video uploaded successfully',
        'filename': 'main.mp4'
    })

@app.route('/api/start_simulation', methods=['POST'])
def start_simulation():
    """Start the rescue simulation"""
    global simulation_running

    if simulation_running:
        return jsonify({'status': 'error', 'message': 'Simulation already running'})

    simulation_running = True

    # Clear the log queue
    while not log_queue.empty():
        try:
            log_queue.get_nowait()
        except queue.Empty:
            break

    # Start simulation in background thread
    thread = threading.Thread(target=run_simulation)
    thread.daemon = True
    thread.start()

    return jsonify({'status': 'success', 'message': 'Simulation started'})

def run_simulation():
    """Run the rescue simulation and capture output"""
    global simulation_running

    try:
        # Run the simulation command
        process = subprocess.Popen(
            ['python', 'rescue_simulation.py', '--scenario', 'fire', '--iterations', '3', '--agents', '2'],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )

        # Stream output to queue
        for line in process.stdout:
            log_queue.put(line.rstrip())

        process.wait()
        log_queue.put('--- SIMULATION COMPLETE ---')

    except Exception as e:
        log_queue.put(f'ERROR: {str(e)}')

    finally:
        simulation_running = False

@app.route('/api/logs')
def stream_logs():
    """Stream simulation logs via Server-Sent Events"""
    def generate():
        while True:
            try:
                # Get log line with timeout
                line = log_queue.get(timeout=1)
                yield f"data: {line}\n\n"
            except queue.Empty:
                # Send heartbeat
                yield f"data: \n\n"
                if not simulation_running and log_queue.empty():
                    break

    return Response(generate(), mimetype='text/event-stream')

@app.route('/api/status')
def get_status():
    """Get current simulation status"""
    return jsonify({
        'running': simulation_running,
        'queue_size': log_queue.qsize()
    })

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static', exist_ok=True)

    print("\n" + "="*70)
    print("EVACUTRACE WEB UI")
    print("="*70)
    print("\nStarting web server...")
    print("Open your browser to: http://localhost:5000")
    print("\nPress Ctrl+C to stop")
    print("="*70 + "\n")

    app.run(debug=True, threaded=True)
