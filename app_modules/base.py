from flask import Blueprint, jsonify

router = Blueprint('base', __name__)

@router.route('/')
def HelloWorld():
    return jsonify('Welcome to AnalyticX')