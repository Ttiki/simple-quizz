from app import create_app

def run_app():
    """
    Run the application.
    """
    app = create_app()
    app.run(debug=True, port=80, host='0.0.0.0')

if __name__ == '__main__':
    run_app()
