import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import func
from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  
  CORS(app, resources={r"/api/*": {"origins": "*"}})

  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, DELETE')
    return response
  

  @app.route('/categories', methods=['GET'])
  def get_categories():
    categories = {category.id: category.type for category in Category.query.order_by(Category.id).all()}

    if len(categories) == 0:
      abort(404)

    return jsonify({
      "success": True,
      "categories": categories,
      "total_categories": len(categories)
    })


  @app.route('/questions', methods=['GET'])
  def get_questions():
    selected_page = request.args.get('page', 1, type=int)
    current_index = selected_page - 1
    items_limit = 10

    questions = [question.format() for question in Question.query.order_by(
        Question.id
    ).limit(items_limit).offset(current_index * items_limit).all()]

    categories = {category.id: category.type for category in Category.query.order_by(
        Category.id).all()}


    if len(questions) == 0 or len(categories) == 0:
      abort(404)

    return jsonify({
      "success": True,
      "questions": questions,
      "total_questions": len(questions),
      "categories": categories,
      "current_category": None
    })


  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):
    question = Question.query.get(question_id)

    if question:
      question.delete()

      return jsonify({
        'success': True
      })
    else: 
      abort(404)


  @app.route('/questions', methods=['POST'])
  def create_question():
    question = request.json.get('question', '')
    answer = request.json.get('answer', '')
    category = request.json.get('category', '')
    difficulty = request.json.get('difficulty', '')

    if question == '' or answer == '' or category == '' or difficulty == '':
      abort(422)

    new_question = Question(
      question = question,
      answer = answer, 
      category = category,
      difficulty = difficulty
    )

    new_question.insert()

    return jsonify({
      'success': True
    })


  @app.route('/questions/search', methods=['POST'])
  def search_questions():
    search_term = request.json.get('searchTerm')

    questions = [question.format() for question in Question.query.filter(Question.question.ilike(f'%{search_term}%')).all()]

    if len(questions) == 0:
      abort(404)

    return jsonify({
      'success': True,
      'questions': questions,
      'total_questions': len(questions),
      'current_category': None
    })


  @app.route('/categories/<int:category_id>/questions', methods=['GET'])
  def get_questions_by_category(category_id):

    questions = [question.format() for question in Question.query.filter(Question.category == category_id).all()]

    if len(questions) == 0:
      abort(404)

    return jsonify({
      'success': True,
      'questions': questions,
      'total_questions': len(questions),
      'current_category': category_id
    })


  @app.route('/quizzes', methods=['POST'])
  def get_quiz_question():
    previous_questions = request.json.get('previous_questions', [])
    quiz_category = request.json.get('quiz_category', None)

    questions = Question.query.filter(Question.id.notin_(previous_questions)).order_by(func.random())

    if quiz_category is not 0:
      questions = questions.filter(Question.category == quiz_category)

    formatted_questions = [question.format() for question in questions]
    print('QUESTION LENGTH', len(formatted_questions))

    if len(formatted_questions) == 0: 
      return jsonify({
        'success': True, 
        'question': None
      })   
    else:
      return jsonify({
        'success': True, 
        'question': formatted_questions[0]
      })      


  # Errors
  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      "success": False, 
      "error": 400,
      "message": "Bad Request"
    }), 400

  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      "success": False, 
      "error": 404,
      "message": "Not found"
    }), 404

  @app.errorhandler(405)
  def not_allowed(error):
    return jsonify({
      "success": False, 
      "error": 405,
      "message": "Method Not Allowed"
    }), 405

  @app.errorhandler(422)
  def unprocessable_entity(error):
    return jsonify({
      "success": False, 
      "error": 422,
      "message": "Method Not Allowed"
    }), 422

  @app.errorhandler(500)
  def server_error(error):
    return jsonify({
      "success": False, 
      "error": 500,
      "message": "Internal Server Error"
    }), 500
  
  return app

    