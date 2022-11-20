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

    const [ questionIndex, setQuestionIndex ] = useState(0)
    const [ questions, setQuestions ] = useState([])
    var flexStylingOption = "flex-styling-50"

    useEffect(() => {
        fetchQuestions()
    }, [])

    // Calls FastAPI to pull questions
    const fetchQuestions = async () => {
        console.log("Questions Fetched!")
        const response = await fetch("http://127.0.0.1:8000/questionnaire/search/")
        const message = await response.json()
        console.log(message)
        setQuestions(message)
    }

    const nextQuestion = () => {
        setQuestionIndex((questionIndex) => questionIndex + 1)
    }

    const previousQuestion = () => {
        setQuestionIndex((questionIndex) => questionIndex - 1)
    }

    const radioAnswerClicked = (e) => {
        var parentDiv = e.currentTarget
        var questionID = e.currentTarget.getAttribute("id");
        var clickedChoice = e.target

        if (clickedChoice.classList.contains("selected")) {
            // Deselect Answer
            clickedChoice.classList.remove("selected")
            // Remove Selection from "questions" state
            removeSelection(questionID, clickedChoice.value)
        } else {
            // Check if something is already selected
            var prevSelected = parentDiv.querySelector(".selected")
            if (prevSelected != null) {
                // Deselect first the previously selected button
                prevSelected.classList.remove("selected")
                removeSelection(questionID, prevSelected.value)
            }
            // Select Answer
            clickedChoice.classList.add("selected")
            // Add Selection to "questions" state
            addSelection(questionID, clickedChoice.value)
        }
    }

    const textSubmission = (e) => {
        var parentDiv = e.currentTarget
        var questionID = e.currentTarget.getAttribute("id");
        var clickedChoice = e.target
        addTextSubmission(questionID, clickedChoice.value)
    }

    // Adds selection to "selectedChoices" array
    const addTextSubmission = (questionID, selectionValue) => {
        let tempQuestions = questions
        tempQuestions.data.map((question, index) => {
            if(question.id == questionID) {
                // If something was already selected
                question.selectedChoices[0] = selectionValue
            }
        });
        setQuestions(tempQuestions)
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

        const response = fetch("http://127.0.0.1:8000/submit/search/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(questions)
        })        
    }

    // Check if questions data is loaded in yet
    if (questions.length == 0) {
        return(
            <div className="container">
                <div className="col-md-7 mt-4 mx-auto">
                    <h1>Loading</h1>
                </div>
            </div>
        )
    } else {
        return (
            <div className="container">
                <div className="d-flex align-items-center justify-content-center h-100">
                    <div className="col-md-7 mt-4">
                        <div className="d-flex flex-column">
                            <h1 className="display-3">Search Questions</h1>
                            <div id="q1" className="question mt-3" onClick={radioAnswerClicked}>
                                <label for="answerOptions">{questions.data[0].question}</label>
                                <ButtonCreate answerOptions={questions.data[0].answerChoices} questionNumber={"q1"} optionType={flexStylingOption} />
                            </div>
                            <div id="q2" className="question mt-3" onClick={radioAnswerClicked}>
                                <label for="answerOptions">{questions.data[1].question}</label>
                                <ButtonCreate answerOptions={questions.data[1].answerChoices} questionNumber={"q2"} optionType={flexStylingOption} />
                            </div>
                            <div id="q3" className="question mt-3" onClick={radioAnswerClicked}>
                                <label for="answerOptions">{questions.data[2].question}</label>
                                <ButtonCreate answerOptions={questions.data[2].answerChoices} questionNumber={"q3"} optionType={flexStylingOption} />
                            </div>
                            <div id="q4" className="question mt-3" onClick={radioAnswerClicked}>
                                <label for="answerOptions">{questions.data[3].question}</label>
                                <ButtonCreate answerOptions={questions.data[3].answerChoices} questionNumber={"q4"} optionType={flexStylingOption} />
                            </div>
                            <div id="q5" className="question mt-3" onChange={textSubmission}>
                                <label for="answerOptions">{questions.data[4].question}</label>
                                <input type="text" id="distance" className="input-box form-control mt-2 w-100" placeholder="Enter your zipcode"></input>
                            </div>
                            <div className="d-flex justify-content-center mt-4 mb-5">
                                <IconContext.Provider value={{ color: "white", size: 20 }}>
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
}

export default SearchQuestions