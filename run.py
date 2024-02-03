from app import create_app

app = create_app()

if __name__ == '__main__':
    # Run the application
    app.run(debug=False, port=80, host='0.0.0.0')
