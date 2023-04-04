import React, { Component } from 'react'
import { useEffect, useState } from 'react'

import * as FaIcons from 'react-icons/fa'
import * as AiIcons from 'react-icons/ai'
import * as BoxIcons from 'react-icons/bi'
import * as BsIcons from "react-icons/bs"

import { IconContext } from 'react-icons'
import { useNavigate } from 'react-router-dom'

import PreviousNextButton from '../components/PreviousNextButton'
import DashboardNavbar from '../components/DashboardComponents/DashboardNavbar';
import LoadingAnimation from '../components/LoadingAnimation'
import CreateQuestion from '../components/CreateQuestion'

import '../css/SearchQuestions.css';

function NewSearchQuestions() {

    const navigate = useNavigate()
    const [ questionIndex, setQuestionIndex ] = useState(0)
    const [ questions, setQuestions ] = useState([])
    const [ answerSelected, setAnswerSelected ] = useState(0)

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

        const response = await fetch("http://localhost:8000/questionnaire/search/", requestOption)
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
        setAnswerSelected(0)
    }

    const previousQuestion = () => {

        var currentQuestion = "q" + (questionIndex + 1)
        var previousQuestion = "q" + questionIndex

        // Delete previous and current selections to reset when previous is clicked
        removeAllSelection(currentQuestion)
        removeAllSelection(previousQuestion)
        setQuestionIndex((questionIndex) => questionIndex - 1)
        setAnswerSelected(0)
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
            setAnswerSelected(0)
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
            setAnswerSelected(1)
        }
    }

    const textSubmission = (e) => {
        var parentDiv = e.currentTarget
        var questionID = e.currentTarget.getAttribute("id");
        var clickedChoice = e.target
        addTextSubmission(questionID, clickedChoice.value)
        setAnswerSelected(1)
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

    // Removes selection from "selectedChoices" array fully
    const removeAllSelection = (questionID) => {
        let tempQuestions = questions
        tempQuestions.data.map((question, index) => {
            if(question.id == questionID) {
                question.selectedChoices.splice(0, 1)
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

        const response = fetch("http://localhost:8000/submit/search/", requestOption)   
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
            <div className="container-fluid search-component">
                <DashboardNavbar />
                <div className="d-flex flex-column">
                    <div className="d-flex align-items-center justify-content-center">
                        <div className="col-md-8 mt-5">
                            <div className="search-main-block">
                                <h1 className="move-medium">Question {questionIndex + 1} / {questions.data.length}</h1>
                                    {
                                        questionIndex == 4 ? 
                                            <div id="q5" className="question mt-3" onChange={textSubmission}>
                                                <label for="answerOptions">{questions.data[4].question}</label>
                                                <input type="text" id="distance" className="input-box form-control mt-2 w-100" placeholder="Enter your zipcode"></input>
                                            </div> 
                                            : 
                                            <CreateQuestion 
                                                question={questions.data[questionIndex]} 
                                                questionNumber={questionIndex} 
                                                radioAnswerClicked={radioAnswerClicked}
                                                flexStylingOption={flexStylingOption}
                                            />
                                    }
                                <div className="d-flex align-items-center justify-content-around mt-5">
                                    {
                                        questionIndex == 0 ? null: 
                                            <button 
                                                id="previousQuestion"
                                                className="btn search-navigation move-medium"
                                                onClick={previousQuestion}>
                                                {"<"}
                                            </button>
                                    }
                                    {
                                        questionIndex >= questions.data.length - 1 ? 
                                            answerSelected == 1 ? 
                                                <button 
                                                    id="submit" 
                                                    className="btn search-navigation move-medium" 
                                                    onClick={submitSelections}>
                                                    Submit
                                                </button>
                                                :
                                                <button 
                                                    id="submit" 
                                                    className="btn search-navigation move-medium disabled" 
                                                    onClick={submitSelections}>
                                                    Submit
                                                </button>

                                        :
                                            questionIndex < questions.data.length - 1 && answerSelected == 1 ? 
                                                <button 
                                                    id="nextQuestion"
                                                    className="btn search-navigation move-medium"
                                                    onClick={nextQuestion}>
                                                    {">"}
                                                </button>
                                                : 
                                                <button 
                                                    id="nextQuestion"
                                                    className="btn search-navigation move-medium disabled"
                                                    onClick={nextQuestion}>
                                                    {">"}
                                                </button>
                                    }
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div> 
        );
    }
}

export default NewSearchQuestions