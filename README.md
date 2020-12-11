# Trivia API

## Introduction

This project is quiz app for whomever wants to use it. It has the ability to pre-populate your database with some questions and categories, plus you can add as many of your own questions as you want!

This is the second project of my Full Stack Web Developer microdegree course through Udacity. This was actually a pretty fun project to work on, minus a few hiccups when initially trying to get it up and running.
If you do decide to take a look at this project I hope you enjoy it as I did!

This follows the [PEP8 style guides](https://www.python.org/dev/peps/pep-0008/). (At least to the best of my ability)

<br>

## Getting Started

### Pre-requisites

This app uses Python3, pip, and Node. So you should already have these installed on your machine. If not, I would recommend going and doing that now.

### Backend

1) To get the backend up and running, first `cd` into the backend folder and run `pip install requirements.txt`. This should download all necessary packages in order to run it.

2) Before starting it you may want to start up a virtualenv using the following commands: 
```
python -m virtualenv env
source env/bin/activate
```
>**Note** Or if your using Windows you will need to replace the second line with:
```
source env/Scripts/activate
```
<br>

3) To actually start up the application run the following commands:
```
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```
>**Note** If you are using Windows and these don't work replace `export` with `set`

This will tell Flask where to look for the app and set it into development mode. This will automatically make it look at the `__init__.py` file inside the `/flaskr` folder.

The application runs on `http://127.0.0.1:5000/` by default and is just the server for the frontend, so you won't see anything on this port in your browser.

### Frontend

Now to get the frontend up and running. Open a new terminal and cd into the `frontend` folder and run the following 

```
npm i  //shorthand for npm install
npm start
```
This will start up the app on [localhost:3000](localhost:3000) by default.

### Testing

To run the tests navigate back into the `backend` folder and run these commands: 

```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```

## API Reference

### Getting Started

- Base URL: This app is currently only able to be run locally. The backend runs on `http://127.0.0.1:5000/` by default.
- Authentication: There is no authentication set up for this app.

### Error Handling

All of the errors you will encounter in this app have been formatted as JSON objects in the following format: 
```json
{
  "success": false,
  "error": 400,
  "message": "Bad Request"
}
```

The following are all of the potential errors you may run into: 

| Code | Message |
| ---- | ------- |
| 400 | Bad Request |
| 404 | Not Found |
| 405 | Method Not Allowed |
| 422 | Not Proccessable |
| 500 | Internal Server Error |

## Endpoints

### GET /categories

- General
  - Returns an object containing all of the categories and the total number of categories
  - URL: `http://127.0.0.1:5000/categories`

```json
{
    "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
    },
    "total_categories": 6,
    "success": true
}
```

### GET /questions

- General 
  - Returns a list of questions, total number of questions, object containing categories, and the current category (should be none).
  - Paginates results into groups of 10, takes a query param `page` to select starting page.
  - URL: `http://127.0.0.1:5000/questions?page=1`

```json
{
    "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
    },
    "current_category": null,
    "questions": [
        {
            "answer": "Apollo 13",
            "category": 5,
            "difficulty": 4,
            "id": 2,
            "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        },
        {
            "answer": "Maya Angelou",
            "category": 4,
            "difficulty": 2,
            "id": 5,
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        },
        {
            "answer": "Edward Scissorhands",
            "category": 5,
            "difficulty": 3,
            "id": 6,
            "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        },
        {
            "answer": "Muhammad Ali",
            "category": 4,
            "difficulty": 1,
            "id": 9,
            "question": "What boxer's original name is Cassius Clay?"
        },
        {
            "answer": "Brazil",
            "category": 6,
            "difficulty": 3,
            "id": 10,
            "question": "Which is the only team to play in every soccer World Cup tournament?"
        },
        {
            "answer": "Uruguay",
            "category": 6,
            "difficulty": 4,
            "id": 11,
            "question": "Which country won the first ever soccer World Cup in 1930?"
        },
        {
            "answer": "George Washington Carver",
            "category": 4,
            "difficulty": 2,
            "id": 12,
            "question": "Who invented Peanut Butter?"
        },
        {
            "answer": "Lake Victoria",
            "category": 3,
            "difficulty": 2,
            "id": 13,
            "question": "What is the largest lake in Africa?"
        },
        {
            "answer": "The Palace of Versailles",
            "category": 3,
            "difficulty": 3,
            "id": 14,
            "question": "In which royal palace would you find the Hall of Mirrors?"
        },
        {
            "answer": "Agra",
            "category": 3,
            "difficulty": 2,
            "id": 15,
            "question": "The Taj Mahal is located in which Indian city?"
        }
    ],
    "success": true,
    "total_questions": 21
}
```

### DELETE /questions/{question_id}

- General
  - Deletes the question with a matching ID if it exists. Just returns a success value.
  - URL: `http://127.0.0.1:5000/questions/{id}`

```json
{
  "success": true
}
```
  
### POST /questions

- General
  - Creates a new question with the given values.
  - Receives data to insert into record in the following format:
  ```json5
    {
      "question": "What is your answer?",
      "answer": "This is my answer.",
      "category": 1, //ID of related category
      "difficulty": 3 //on a scale of 1-5
    }
  ```
  - Returns a success response.
  - URL: `http://127.0.0.1:5000/questions`

```json
{
  "success": true
}
```

### POST /questions/search

- General
  - Returns a list of questions that contain the search term somewhere in the question (case insensitive) and the total questions found.
  - Recieves data in the following format: 
  ```json
    {
      "searchTerm": "title"
    }
  ```
  - URL: `http://127.0.0.1:5000/questions/search`

```json
{
    "current_category": null,
    "questions": [
        {
            "answer": "Maya Angelou",
            "category": 4,
            "difficulty": 2,
            "id": 5,
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        },
        {
            "answer": "Edward Scissorhands",
            "category": 5,
            "difficulty": 3,
            "id": 6,
            "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        }
    ],
    "success": true,
    "total_questions": 2
}
```

### GET /categories/{category_id}/questions

- General
  - Returns a list of questions for a given category, total questions, and the selected category ID.
  - URL: `http://127.0.0.1:5000/categories/{id}/questions`
```json
{
    "current_category": 1,
    "questions": [
        {
            "answer": "The Liver",
            "category": 1,
            "difficulty": 4,
            "id": 20,
            "question": "What is the heaviest organ in the human body?"
        },
        {
            "answer": "Alexander Fleming",
            "category": 1,
            "difficulty": 3,
            "id": 21,
            "question": "Who discovered penicillin?"
        },
        {
            "answer": "Blood",
            "category": 1,
            "difficulty": 4,
            "id": 22,
            "question": "Hematology is a branch of medicine involving the study of what?"
        },
        {
            "answer": "5",
            "category": 1,
            "difficulty": 1,
            "id": 24,
            "question": "What is the answer?"
        },
        {
            "answer": "Still 5",
            "category": 1,
            "difficulty": 2,
            "id": 25,
            "question": "NOW, what is the answer?"
        }
    ],
    "success": true,
    "total_questions": 5
}
```

### POST /quizzes

- General 
  - Returns a random question in the given category (if provided) that is not one of the previous questions (if provided)
  - Recieves data in the following format: 
  ```json
    {
     "previous_questions": [3, 6, 2], //ID's of the previous questions
     "quiz_category": 2 //ID of the selected category (can be null)
    }
  ```
  - URL: `http://127.0.0.1:5000/quizzes`

```json
{
    "question": {
        "answer": "Alexander Fleming",
        "category": 1,
        "difficulty": 3,
        "id": 21,
        "question": "Who discovered penicillin?"
    },
    "success": true
}
```

### Authors

While the shell of the app was all done by the folks over at Udacity, the implementation was done by yours truly. <br>
Trevor Hallett

### Acknowledgements

While I was pretty proud of how much of this app I did by myself, there is no way I could have done this without the help of the fellow students.
They indirectly helped me out by asking questions that I had so I was able to figure everything out just by reading the questions other students posted without having to post any of my own.