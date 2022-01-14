from flask import Flask

def init_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    #register blue prints
    from app.employee.employee_bp import emp_bp
    app.register_blueprint(emp_bp)
    
    return app

