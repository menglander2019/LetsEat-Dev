from .data_generation.data_gen_constants import *

profile_questions = [
    {
        "id": "q1",
        "question": "What are your cuisine preferences?",
        "answerChoices": list(cuisine_groups.keys()),
        "selectedChoices": []
    },
    {
        "id": "q2",
        "question": "Any food restrictions or allergies?",
        "answerChoices": list(restrictions_dict.keys()),
        "selectedChoices": []
    },
    {
        "id": "q3",
        "question": "What cuisine do you want not recommended?",
        "answerChoices": list(cuisine_groups.keys()),
        "selectedChoices": []
    }
]

search_questions = [
    {
        "id": "q1",
        "question": "What is the occasion?",
        "answerChoices": occasions,
        "selectedChoices": []
    },
    {
        "id": "q2",
        "question": "How many people?",
        "answerChoices": num_people,
        "selectedChoices": []
    },
    {
        "id": "q3",
        "question": "What type of meal?",
        "answerChoices": meals,
        "selectedChoices": []
    },
    {
        "id": "q4",
        "question": "What is the price range?",
        "answerChoices": price_ranges,
        "selectedChoices": []
    },
    {
        "id": "q5",
        "question": "Zipcode",
        "selectedChoices": []
    }
]

group_search_questions = [
    {
        "id": "q1",
        "question": "What is the occasion?",
        "answerChoices": group_occasions,
        "selectedChoices": []
    },
    {
        "id": "q2",
        "question": "What type of meal?",
        "answerChoices": meals,
        "selectedChoices": []
    },
    {
        "id": "q3",
        "question": "What is the price range?",
        "answerChoices": price_ranges,
        "selectedChoices": []
    },
    {
        "id": "q4",
        "question": "Zipcode",
        "selectedChoices": []
    }
]

createprofile_questions = [
    {
        "id": "q1",
        "question": "Enter your email",
        "answerChoices": [],
        "selectedChoices": []
    },
    {
        "id": "q2",
        "question": "Create a password",
        "answerChoices": [],
        "selectedChoices": []
    },
    {
        "id": "q3",
        "question": "What should we call you?",
        "answerChoices": [],
        "selectedChoices": []
    },
    {
        "id": "q4",
        "question": "Enter your date of birth",
        "answerChoices": [],
        "selectedChoices": []
    },
    {
        "id": "q5",
        "question": "What is your gender?",
        "answerChoices": [],
        "selectedChoices": []
    }
]

login_questions = [
    {
        "id": "q1",
        "question": "Enter your email",
        "answerChoices": [],
        "selectedChoices": []
    },
    {
        "id": "q2",
        "question": "Enter your password",
        "answerChoices": [],
        "selectedChoices": []
    }
]