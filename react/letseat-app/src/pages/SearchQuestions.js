import React, { Component } from 'react'
import { useEffect, useState } from 'react'

import * as FaIcons from 'react-icons/fa'
import * as AiIcons from 'react-icons/ai'
import * as BoxIcons from 'react-icons/bi'
import * as BsIcons from "react-icons/bs"

import { IconContext } from 'react-icons'
import { useNavigate } from 'react-router-dom'

import PreviousNextButton from '../components/PreviousNextButton'
import ButtonCreate from '../components/ButtonCreate'
import DashboardNavbar from '../components/DashboardComponents/DashboardNavbar';
import LoadingAnimation from '../components/LoadingAnimation'


function SearchQuestions() {

    const navigate = useNavigate()
    const [ questionIndex, setQuestionIndex ] = useState(0)
    const [ questions, setQuestions ] = useState([])
    var flexStylingOption = "flex-styling-50"

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
        const response = await fetch("http://ec2-3-84-237-203.compute-1.amazonaws.com:8000/questionnaire/search/", requestOption)
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

        e.preventDefault()

        console.log(questions)

        const requestOption = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            credentials: "include",
            body: JSON.stringify(questions)
        }

        const response = fetch("http://ec2-3-84-237-203.compute-1.amazonaws.com:8000/submit/search/", requestOption)   
            .then(response => {
                if (response.ok) {
                    navigate("/restaurantsearch") 
                } else {
                    console.log("Error Posting!")
                }
            })
            .catch(error => {
                console.log("Error Recommending!")
            })
    }

    if (localStorage.getItem("token") == null) {
        return navigate("/")
    } else if (questions.length == 0) {
        return (<LoadingAnimation />)
    } else {
        return (
            <div className="container-fluid">
                <DashboardNavbar />
                <div className="d-flex justify-content-center h-100">
                    <div className="col-md-6 mt-5">
                        <div className="d-flex flex-column">
                            <h1 className="display-5 colfax-regular">Search Questions</h1>
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