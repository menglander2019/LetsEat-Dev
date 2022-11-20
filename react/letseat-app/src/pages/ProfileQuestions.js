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

    // Temporary Filler Arrays
    //var cuisineChoices = ["American", "Mexican", "French", "Chinese", "Japanese", "Italian", "Korean", "Thai"]
    //var allergyChoices = ["Gluten", "Eggs", "Dairy", "Peanuts", "N/A"]

    useEffect(() => {
        fetchQuestions()
    }, [])

    // Calls FastAPI to pull questions
    const fetchQuestions = async () => {
        console.log("Questions Fetched!")
        const response = await fetch("http://127.0.0.1:8000/questionnaire/profile/")
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
                        <div id="profileQuestions">
                            <div className="d-flex flex-column">
                                <h1 className="display-3">Profile Questions</h1>
                                <div id="q1" className="question mt-3" onClick={answerClicked}>
                                        <label for="answerOptions">{questions.data[0].question}</label>
                                        <ButtonCreate answerOptions={questions.data[0].answerChoices} questionNumber={"q1"} optionType="profileOption" />
                                </div>
                                <div id="q2" className="question mt-3" onClick={answerClicked}>
                                    <label for="answerOptions">{questions.data[1].question}</label>
                                    <ButtonCreate answerOptions={questions.data[1].answerChoices} questionNumber={"q2"} optionType="profileOption" />
                                </div>
                                <div id="q3" className="question mt-3" onClick={answerClicked}>
                                    <label for="answerOptions">{questions.data[2].question}</label>
                                    <ButtonCreate answerOptions={questions.data[2].answerChoices} questionNumber={"q3"} optionType="profileOption" />
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
            </div>
        );
    }
}


export default ProfileQuestions