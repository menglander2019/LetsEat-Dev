import React, { Component } from 'react'
import { useEffect, useState } from 'react'

import * as FaIcons from 'react-icons/fa'
import * as AiIcons from 'react-icons/ai'
import * as BoxIcons from 'react-icons/bi'
import * as BsIcons from "react-icons/bs"

import { IconContext } from 'react-icons'

import PreviousNextButton from '../components/PreviousNextButton'
import ButtonCreate from '../components/ButtonCreate'

function SearchQuestions() {

    var questionBank = [
        {
            id: 0,
            question: "What is the occasion?",
            answers: ["Friends", "Family", "Date", "Work"],
            questionId: "0001",
            selected: ""
        },
        {
            id: 1,
            question: "How many people?",
            answers: ["1", "2", "3", "4+"],
            questionId: "0002",
            selected: ""
        },
        {
            id: 2,
            question: "What kind of meal?",
            answers: ["Breakfast", "Lunch", "Dinner", "Dessert"],
            questionId: "0003",
            selected: ""
        },
        {
            id: 3,
            question: "What's the price range?",
            answers: ["$", "$$", "$$$", "N/A"],
            questionId: "0004",
            selected: ""
        }
    ];
    const [ questions, setQuestions ] = useState([])
    const [ questionIndex, setQuestionIndex ] = useState(0)

    useEffect(() => {
        fetchQuestions()
    }, [])

    // Calls FastAPI to pull questions
    const fetchQuestions = async () => {
        console.log("Questions Fetched!")
        const response = await fetch("http://127.0.0.1:8000/questionnaire/search/")
        const message = await response.json()
        setQuestions(message)
    }

    const nextQuestion = () => {
        setQuestionIndex((questionIndex) => questionIndex + 1)
    }

    const previousQuestion = () => {
        setQuestionIndex((questionIndex) => questionIndex - 1)
    }

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
                // If something was already selected
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

        const response = fetch("http://127.0.0.1:8000/submit/questionnaire/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(questions)
        })        
    }

    return (
        <div className="container">
            <div className="col-md-7 mt-4 mx-auto">
                <h1 className="display-3">Search Questions</h1>
                <div id="searchQuestions">
                    <div className="row mt-3">
                        <div id="q1" className="question" onClick={answerClicked}>
                            <label for="answerOptions">What is the occasion?</label>
                            <ButtonCreate answerOptions={questionBank[0].answers} questionNumber={"q1"} colNumber={6} />
                        </div>
                    </div>
                    <div className="row mt-3">
                        <div id="q2" className="question" onClick={answerClicked}>
                            <label for="answerOptions">How many people?</label>
                            <ButtonCreate answerOptions={questionBank[1].answers} questionNumber={"q2"} colNumber={6} />
                        </div>
                    </div>
                    <div className="row mt-3">
                        <div id="q3" className="question" onClick={answerClicked}>
                            <label for="answerOptions">What type of meal?</label>
                            <ButtonCreate answerOptions={questionBank[2].answers} questionNumber={"q3"} colNumber={6} />
                        </div>
                    </div>
                    <div className="row mt-3">
                        <div id="q4" className="question" onClick={answerClicked}>
                            <label for="answerOptions">What is the price range?</label>
                            <ButtonCreate answerOptions={questionBank[3].answers} questionNumber={"q4"} colNumber={6} />
                        </div>
                    </div>
                    <div className="row mt-3">
                        <div id="q5" className="question" onClick={answerClicked}>
                            <label for="answerOptions">Distance Preference</label>
                            <p>Google Maps Pin Drop Here</p>
                            <p>Mile Selecting Slider Here</p>
                        </div>
                    </div>
                    <div className="row mt-4 mb-5">
                        <div className="col-md-12 mx-auto">
                            <IconContext.Provider value={{ color: "white", size: 25 }}>
                                <button 
                                    id="submit"
                                    className="btn btn-primary submit w-100" 
                                    onClick={submitSelections}>
                                    Search
                                </button>
                            </IconContext.Provider>
                        </div>
                    </div>
                </div> 
            </div>
        </div> 
    );
}
  
/**
 * <PreviousNextButton 
        questionIndex={questionIndex}
        previousQuestion={previousQuestion}
        nextQuestion={nextQuestion}
        numQuestions={questionBank.length}
    />
 */

export default SearchQuestions