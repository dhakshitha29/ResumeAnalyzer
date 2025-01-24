from flask import Blueprint, request, jsonify
from app.utils.file_handler import save_file
from app.services.parser import parse_resume
from app.services.extractor import extract_details
from app.services.question_generator import generate_questions
from app.db import get_db
import datetime

api = Blueprint('api', __name__)
db = get_db()

@api.route('/api/analyze-resume', methods=['POST'])
def analyze_resume():
    print("Route hit")  # Add this for debugging
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Handle file saving and further processing
    upload_folder = './uploads'
    file_path = save_file(file, upload_folder)
    print(f"File saved to: {file_path}")  # Check file saving

    # Resume processing logic here
    text = parse_resume(file_path)
    details = extract_details(text)
    print(f"Extracted details: {details}")  # Check extracted details
    questions = generate_questions(details['Skills'],details['Activities'])
    print(f"Generated questions: {questions}")  # Check generated questions

    # Save to DB
    resume_data = {
        "resumeData": details,
        "questions": questions,
        "uploadedAt": datetime.datetime.now()
    }
    result = db.resumes.insert_one(resume_data)
    print(f"Resume saved with ID: {result.inserted_id}")  # Check DB insertion

    return jsonify({
        'details': details,
        'questions': questions,
        'message': 'Resume successfully analyzed and saved.',
        'resumeId': str(result.inserted_id)
    })
