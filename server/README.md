# Quiz
This is a quiz app built with django. It is a group assignment

## Features
    1. Every authenticated user can create a quiz
    2. Every authenticated can answer a quiz only once
    3. Scores gotten for a right answer is subject to the time it took to answer the question


## Routes
    /quiz   - list of all quizzes. This include their questions and possible answers etc
    /quiz/<int:pk>/ - Retrieves data for just one quiz object
    /quiz/create/   - Endpoint for creating a quiz
    /Quiz/solution/create/  - Endpoint for submitting results from taking a quiz
    /Quiz/solution/ - Endpoint to view details of a person's solution. This is visible to only the user that took the quiz


    /account/api-views/login/    - User login 
    /account/api-views/logout/   - User logout
    /account/api-views/create/   - User Registration