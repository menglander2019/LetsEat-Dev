import React, { Component } from 'react'
import { useEffect, useState } from 'react'
import { Link, Navigate } from 'react-router-dom'

import HomeNavbar from '../components/HomeComponents/HomeNavbar';
import SearchQuestions from './SearchQuestions';


function CreateAccount() {

    const [ questions, setQuestions ] = useState([])

    useEffect(() => {
        fetchQuestions()
    }, [])

    // Calls FastAPI to pull questions
    const fetchQuestions = async () => {
        const response = await fetch("http://127.0.0.1:8000/questionnaire/login/")
        const message = await response.json()
        console.log(message)
        setQuestions(message)
    }

    const textSubmission = (e) => {
        var parentDiv = e.currentTarget
        var questionID = e.currentTarget.getAttribute("id");
        var clickedChoice = e.target
        addTextSubmission(questionID, clickedChoice.value)
    }

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

    const checkInputSubmissions = () => {
        let tempQuestions = questions
        let checkStatus = 1
        tempQuestions.data.map((question, index) => {
            if(question.selectedChoices.length == 0) {
                checkStatus = 0
            }
        })
        return checkStatus
    }
    const submitSelections = async (e) => {
        e.preventDefault()
        if (checkInputSubmissions() == 1) {
            const requestOption = {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(questions)
            }
            const response = await fetch("http://127.0.0.1:8000/checkLogin", requestOption)
            const data = await response.json()
            console.log(data.status)
            console.log(data.token)
            
            if (data.status == 1) {
                console.log("Logged In Success")
                localStorage.setItem("token", data.token)
                console.log(localStorage.getItem("token"))
            } else {
                // Temporary invalid code
                console.log("Logged In Failed")
            }
        } else {
            // Temporary invalid code
            console.log("Logged In Failed")
        }

    }

    if (localStorage.getItem("token") != null) {
        console.log("Inside")
        return ( <Navigate to="/dashboard" /> )
    } else {
        return (
            <>
            <div className="container-fluid">
                <HomeNavbar />
                <div className="d-flex align-items-center justify-content-center h-100">
                    <div className="col-md-3">
                        <form onSubmit={submitSelections}>
                            <div className="d-flex flex-column">
                                <div className="row mt-4">
                                    <h3 className="colfax-regular">Welcome to LetsEat!</h3>
                                </div>
                                <div id="q1" className="question input-group mt-2" onChange={textSubmission}>                            
                                    <label for="email">Log In</label>
                                    <input type="text" id="email" className="form-control login-box w-100 mt-3" placeholder="Enter email" required></input>          
                                </div>
                                <div id="q2" className="question mt-2" onChange={textSubmission}>                            
                                    <input type="text" id="password" className="login-box form-control w-100 mt-3" placeholder="Enter password" required></input>
                                </div>
                                <div className="row mt-4">
                                    <div className="col-md-12">
                                        <button 
                                            id="submit"
                                            className="btn btn-primary submit w-100"
                                            type="submit">
                                            Log In
                                        </button>
                                    </div>
                                </div>
                                <div className="row mt-4">
                                    <div className="col-md-12">
                                        <p className="colfax-regular">
                                            Don't have an account?
                                            <Link to="/createaccount">
                                                <span>Sign Up</span>
                                            </Link>
                                        </p>
                                    </div>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
            </>
        );
    }
}
  

export default CreateAccount