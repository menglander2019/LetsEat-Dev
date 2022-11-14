import React, { Component } from 'react'
import { useEffect, useState } from 'react'

import * as FaIcons from 'react-icons/fa'
import * as AiIcons from 'react-icons/ai'
import * as BoxIcons from 'react-icons/bi'
import { IconContext } from 'react-icons'

import PreviousNextButton from '../components/PreviousNextButton'
import ButtonCreate from '../components/ButtonCreate'
import { renderMatches } from 'react-router-dom'

function ProfileQuestions() {

    const [ questionIndex, setQuestionIndex ] = useState(0)
    const [ questions, setQuestions ] = useState([])
    var numQuestions = 3

    var cuisineChoices = ["American", "Mexican", "French", "Chinese", "Japanese", "Italian", "Korean", "Thai"]
    var allergyChoices = ["Gluten", "Eggs", "Dairy", "Peanuts", "N/A"]

    const nextQuestion = () => {
        setQuestionIndex((questionIndex) => questionIndex + 1)
    }

    const previousQuestion = () => {
        setQuestionIndex((questionIndex) => questionIndex - 1)
    }

    useEffect(() => {
        fetchQuestions()
    }, [])

    const answerClicked = (e) => {
        var questionID = e.currentTarget.getAttribute("id");
        var clickedChoice = e.target;

        if (clickedChoice.classList.contains("selected")) {
            // Deselect Answer
            clickedChoice.classList.remove("selected");
            // Remove Selection from "questions" state
            removeSelection(questionID, clickedChoice.value)
        } else {
            // Select Answer
            clickedChoice.classList.add("selected");
            // Add Selection to "questions" state
            addSelection(questionID, clickedChoice.value)
        }
    }

    // Adds selection to "selectedChoices" array
    const addSelection = (questionID, selectionValue) => {
        let tempQuestions = questions
        tempQuestions.data.map((question, index) => {
            if(question.id == questionID) {
                question.selectedChoices.push(selectionValue)
            }
        });
        setQuestions(tempQuestions)
    }

    // Removes selection from "selectedChoices" array
    const removeSelection = (questionID, selectionValue) => {
        let tempQuestions = questions
        tempQuestions.data.map((question, index) => {
            if(question.id == questionID) {
                question.selectedChoices.map((choice, choiceIndex) => {
                    if (choice == selectionValue) {
                        question.selectedChoices.splice(choiceIndex, 1)
                    }
                })
            }
        });
        setQuestions(tempQuestions)
    }

    // Submits user selection to FastAPI
    const submitSelections = (e) => {

        console.log(questions)

        const response = fetch("http://127.0.0.1:8000/submit/profile/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(questions)
        })
        console.log(response)        
    }

    // Calls FastAPI to pull questions
    const fetchQuestions = async () => {
        console.log("Questions Fetched!")
        const response = await fetch("http://127.0.0.1:8000/questionnaire/profile/")
        const message = await response.json()
        setQuestions(message)
    }

    
    return (
        <div className="container">
            <div className="col-md-7 mt-4 mx-auto">
                <h1 className="display-3">Profile Questions</h1>
                <div id="profileQuestions">
                    <div className="row mt-3">
                        <div id="q1" className="question" onClick={answerClicked}>
                            <label for="answerOptions">"Temporary Question 1"</label>
                            <ButtonCreate answerOptions={cuisineChoices} questionNumber={"q1"} colNumber={4} />
                        </div>
                    </div>
                    <div className="row mt-3">
                        <div id="q2" className="question" onClick={answerClicked}>
                            <label for="answerOptions">Any food restrictions or allergies?</label>
                            <ButtonCreate answerOptions={allergyChoices} questionNumber={"q2"} colNumber={4} />
                        </div>
                    </div>
                    <div className="row mt-3">
                        <div id="q3" className="question" onClick={answerClicked}>
                            <label for="answerOptions">What cuisine do you want not recommended?</label>
                            <ButtonCreate answerOptions={cuisineChoices} questionNumber={"q3"} colNumber={4} />
                        </div>
                    </div>
                    <div className="row mt-4 mb-5">
                        <div className="col-md-12 mx-auto">
                            <IconContext.Provider value={{ color: "white", size: 15 }}>
                                <button 
                                    id="submit" 
                                    className="btn btn-primary submit w-100 inactive" 
                                    onClick={submitSelections}>
                                    <FaIcons.FaCheck />
                                </button>
                            </IconContext.Provider>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}


export default ProfileQuestions