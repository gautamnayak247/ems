from flask import Blueprint,make_response
from app.employee.models import Employee

emp_bp = Blueprint("employee", __name__, url_prefix= "/api/v1/employees")

@emp_bp.route("/", methods=["GET"])
def get_all_employees():
    return "all employees"

@emp_bp.route("/<id>", methods=["GET"])
def get_employee_by_id(id):
    emp = Employee(id,"gautam","nayak",29)
    return make_response(emp.id)