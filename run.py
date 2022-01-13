from app import create_app

if __name__ == "__main__":
    print("main called")
    ems_app = create_app()
    ems_app.run(host='127.0.168.1', port=8080, debug=True)