import React, { Component } from 'react'
import { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'

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

import '../css/ProfileQuestions.css';

const JoinGroup = () => {

    const { host } = useParams()

    const [ hostID, setHostID ] = useState([])
    const [ hostName, setHostName ] = useState("")

    const [ questionIndex, setQuestionIndex ] = useState(0)
    const [ questions, setQuestions ] = useState([])
    const [ answerSelected, setAnswerSelected ] = useState(0)

    var flexStylingOption = "flex-styling-50"

    useEffect(() => {
        setHostID([])
        hostID.push({"id": host})
        fetchQuestions()
        getHostUsername()
    }, [])

    // Checks if user has already created a group
    const getHostUsername = async () => {

        const requestOption = {
            method: "POST",
            credentials: "include",
            headers: { "Content-Type": "application/json"},
            body: JSON.stringify(hostID[0])
        }

        const response = await fetch("http://ec2-54-160-112-17.compute-1.amazonaws.com:8000/getGroupHostName", requestOption)
            .then(async response => {
                const data = await response.json()
                if (response.ok) {
                    setHostName(data.host_name)
                } else {
                    console.log(data)
                }
            })
            .catch(error => {
                console.log("Error!")
            })
    }
    // Calls FastAPI to pull questions
    const fetchQuestions = async () => {
        console.log("Questions Fetched!")
        const requestOption = {
            method: "GET",
            credentials: "include",
            headers: { "Content-Type": "application/json"}
        }

        const response = await fetch("http://ec2-54-160-112-17.compute-1.amazonaws.com:8000/questionnaire/profile/", requestOption)
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

    const answerClicked = (e) => {
        var parentDiv = e.currentTarget
        var questionID = e.currentTarget.getAttribute("id");
        var clickedChoice = e.target

        if (clickedChoice.classList.contains("selected")) {
            // Deselect Answer
            clickedChoice.classList.remove("selected");
            // Remove Selection from "questions" state
            removeSelection(questionID, clickedChoice.value)

            var prevSelected = parentDiv.querySelector(".selected")
            if (prevSelected == null) {
                // Disable next button
                setAnswerSelected(0)
            }

        } else {
            // Select Answer
            clickedChoice.classList.add("selected");
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
                        question.selectedChoices.splice(choiceIndex, choiceIndex+1)
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
                question.selectedChoices.splice(0, question.selectedChoices.length)
            }
        });
        setQuestions(tempQuestions)
    }

    // Submits user selection to FastAPI
    const submitSelections = (e) => {

        e.preventDefault()

        console.log(questions)
        var hostInfo = {"hostID": host}
        questions.data.push(hostInfo)

        const requestOption = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            credentials: "include",
            body: JSON.stringify(questions)
        }

        const response = fetch("http://ec2-54-160-112-17.compute-1.amazonaws.com:8000/joinGroup/", requestOption)   
            .then(response => {
                if (response.ok) {
                    console.log("Submitted Response!")
                } else {
                    console.log("Error Posting!")
                }
            })
            .catch(error => {
                console.log("Error Recommending!")
            })
    }

    if (questions.length == 0) {
        return (<LoadingAnimation />)
    } else {
        return (
            <div className="container-fluid profile-component">
            <div className="d-flex flex-column">
                <div className="d-flex align-items-center justify-content-center">
                    <div className="col-md-8 mt-5">
                        <h1 className="white-theme">{hostName}'s Group</h1>
                        <div className="profile-main-block">
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
                                            radioAnswerClicked={answerClicked}
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
export default JoinGroup