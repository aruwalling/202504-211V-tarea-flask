from flask import Blueprint, request, Response, jsonify
import app.database as db

user_bp = Blueprint('user', __name__, url_prefix='/api/v1')

REQUIRED_FILES_POST = ['email',"password","username"]

@user_bp.route("/user")
def get_all():
    return jsonify(db.find_all())

@user_bp.route("/user/<int:user_id>",methods=["GET"])
def get_by_id(user_id):
    
    user = db.find_by_id(user_id)
    if user:
        return jsonify(user)
    else:
        return jsonify({"errorMessage":"No record found"}),404

@user_bp.route("/user", methods=["POST"])
def post_user():
    data = request.get_json()
    if set(data.keys()) != set(REQUIRED_FILES_POST):
        return jsonify({"error": "Invalid json structure"}), 400
    new_user = db.insert_user(data)
    return jsonify(new_user),200

@user_bp.route("/user/<int:user_id>", methods=["PUT"])
def put_user(user_id):
    data = request.get_json()
    if  not set(data.keys()).issubset(set(REQUIRED_FILES_POST)):
        return jsonify({"error": "Invalid json structure"}), 400
    user = db.find_by_id(user_id)
    if not user:
        return jsonify({"errorMessage":"No record found"}),404
    
    for k,v in data.items():
        user[k]=v    

    db.update_user(user)
    return Response(status=204)

@user_bp.route("/user/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = db.find_by_id(user_id)
    if not user:
        return jsonify({"errorMessage":"No record found"}),404
    db.delete_user(user_id)
    return Response(status=204)

