from flask import Flask

def create_app():
    app = Flask(__name__)

    #register blue prints
    from app.employee.employee_bp import emp_bp
    app.register_blueprint(emp_bp)
    return app

