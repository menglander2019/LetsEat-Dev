import React, { Component } from 'react'
import { useEffect, useState } from 'react'
import { renderMatches, useNavigate } from 'react-router-dom'

import * as FaIcons from 'react-icons/fa'
import * as AiIcons from 'react-icons/ai'
import * as BoxIcons from 'react-icons/bi'
import { IconContext } from 'react-icons'

import PreviousNextButton from '../components/PreviousNextButton'
import ButtonCreate from '../components/ButtonCreate'
import DashboardNavbar from '../components/DashboardComponents/DashboardNavbar';


function ProfileQuestions() {

    const navigate = useNavigate()
    const [ questionIndex, setQuestionIndex ] = useState(0)
    const [ questions, setQuestions ] = useState([])
    
    var numQuestions = 3
    var flexStylingOption = "flex-styling-33"

    useEffect(() => {
        fetchQuestions()
    }, [])

    // Calls FastAPI to pull questions
    const fetchQuestions = async () => {
        console.log("Questions Fetched!")
        const requestOption = {
            method: "GET",
            credentials: "include",
            headers: { "Content-Type": "application/json"}
        }

        await fetch("http://localhost:8000/questionnaire/profile/", requestOption)
            .then(async response => {
                const data = await response.json()
                if (response.ok) {
                    setQuestions(data)
                } else {
                    console.log("Error!")
                }
            })
            .catch(error => {
                console.log("Error!")
            })
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
    const submitSelections = async (e) => {

        e.preventDefault()
        const requestOption = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            credentials: "include",
            body: JSON.stringify(questions)
        }

        await fetch("http://localhost:8000/submit/profile/", requestOption)
            .then(async response => {
                const data = await response.json()

                if (response.ok) {
                    navigate("/dashboard")
                    // navigate("/searchquestions")
                } else {
                    console.log("Error!")
                }
            })
            .catch(error => {
                console.log("Error!")
            })
    }

    if (localStorage.getItem("token") == null) {
        return navigate("/")
    } else if (questions.length == 0) {
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
                                <h1 className="display-3 colfax-regular">Profile Questions</h1>
                                <div id="q1" className="question mt-3" onClick={answerClicked}>
                                        <label for="answerOptions">{questions.data[0].question}</label>
                                        <ButtonCreate answerOptions={questions.data[0].answerChoices} questionNumber={"q1"} optionType={flexStylingOption} />
                                </div>
                                <div id="q2" className="question mt-3" onClick={answerClicked}>
                                    <label for="answerOptions">{questions.data[1].question}</label>
                                    <ButtonCreate answerOptions={questions.data[1].answerChoices} questionNumber={"q2"} optionType={flexStylingOption} />
                                </div>
                                <div id="q3" className="question mt-3" onClick={answerClicked}>
                                    <label for="answerOptions">{questions.data[2].question}</label>
                                    <ButtonCreate answerOptions={questions.data[2].answerChoices} questionNumber={"q3"} optionType={flexStylingOption} />
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

// Color: #87ae73 GREEN


export default ProfileQuestions