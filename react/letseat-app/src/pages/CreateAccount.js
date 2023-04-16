import React, { Component } from 'react'
import { useEffect, useState } from 'react'

import SignUpNavbar from '../components/SignUpComponents/SignUpNavbar';

import url from '../WebsiteURL'

function CreateAccount() {

    const [ questions, setQuestions ] = useState([])
    const [ birthDate, setBirthDate ] = useState([3])
    const [ accountCreateStatus, setAccountCreateStatus ] = useState(0)

    const handleSubmitButton = () => {
        alert("Account Create!")
    }

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
        const response = await fetch(url + "questionnaire/createprofile/", requestOption)
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

    const birthDateSubmission = (e) => {
        var questionID = e.target.getAttribute("id");
        var currentBirthDate = birthDate
        if (questionID == "month") {
            birthDate[1] = e.target.value
            setBirthDate(currentBirthDate)
        } else if (questionID == "day") {
            let day = e.target.value;
            if (day.length == 1) {
                birthDate[2] = '0' + e.target.value
            } else if (day.length == 2) {
                birthDate[2] = e.target.value
            }
            setBirthDate(currentBirthDate)
        } else if (questionID == "year") {
            birthDate[0] = e.target.value
            setBirthDate(currentBirthDate)
        }

        let concatBirthDate = birthDate[0] + '-' + birthDate[1] + '-' + birthDate[2]
        addTextSubmission("q4", concatBirthDate)
    }

    const answerClicked = (e) => {
        var questionID = e.target.getAttribute("id");
        var clickedChoice = e.target.value;
        console.log(clickedChoice)
        addTextSubmission(questionID, clickedChoice)
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
        console.log(questions)
        if (checkInputSubmissions() == 1) {
            const requestOption = {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                credentials: "include",
                body: JSON.stringify(questions)
            }

            await fetch(url + "createprofile", requestOption)
                .then(async response => {
                    const data = await response.json()
                    if (response.ok) {
                        setAccountCreateStatus(1)
                    }
                })
                .catch(error => {
                    console.log("Error!")
                })
        } else {
            setAccountCreateStatus(2)
            console.log("Account Creation Error!")
        }
    }

    return (
        <div className="container-fluid">
            <SignUpNavbar />
            <div className="d-flex justify-content-center h-100 mb-5">
                <div className="col-md-4 mt-2">
                    <form onSubmit={submitSelections}>
                        <div className="d-flex flex-column">
                            <h4 className="sf-pro-regular text-center mt-3">Sign up for free to discover your new favorite restaurant.</h4>
                            <div id="q1" className="question input-group mt-3" onChange={textSubmission}>                            
                                <label for="email">Enter your email</label>
                                <input type="text" id="email" className="form-control input-box w-100" placeholder="Enter an email" required></input>
                                <small id="nameHelp" className="form-text text-muted">We'll never share your email with anyone else.</small>
                            </div>
                            <div id="q2" className="question input-group mt-3" onChange={textSubmission}>                            
                                <label for="password">Create a password</label>
                                <input type="text" id="password" className="input-box  form-control w-100" placeholder="Create a password" required></input>
                            </div>
                            <div id="q3" className="question input-group mt-3" onChange={textSubmission}>                            
                                <label for="name">What should we call you?</label>
                                <input type="text" id="name" className="input-box form-control w-100" placeholder="Enter a profile name" required></input>
                                <small id="profileNameHelp" className="form-text text-muted">We recommend using your first name.</small>
                            </div>
                            <div id="q4" className="question input-group mt-3" required>                            
                                <label>Enter your date of birth</label>
                                <div className="d-flex flex-row justify-content-between">
                                    <select id="month" onChange={birthDateSubmission} className="input-box form-select flex-styling-33" required>
                                        <option selected disabled value="">Month</option>
                                        <option value="01">January</option>
                                        <option value="02">February</option>
                                        <option value="03">March</option>
                                        <option value="04">April</option>
                                        <option value="05">May</option>
                                        <option value="06">June</option>
                                        <option value="07">July</option>
                                        <option value="08">August</option>
                                        <option value="09">September</option>
                                        <option value="10">October</option>
                                        <option value="11">November</option>
                                        <option value="12">December</option>
                                    </select>
                                    <input type="text" id="day" onChange={birthDateSubmission} className="input-box form-control flex-styling-33" maxLength="2" inputMode="numeric" placeholder="DD" required></input>
                                    <input type="text" id="year" onChange={birthDateSubmission} className="input-box form-control flex-styling-33" maxLength="4" inputMode="numeric" placeholder="YYYY" required></input>
                                </div>
                            </div>
                            <div id="q5-gender" className="question input-group mt-3" required>                            
                                <label>What is your gender?</label><br />
                                <select id="q5" onChange={answerClicked} className="input-box form-select w-100" required>
                                    <option selected disabled value="">Select</option> 
                                    <option value="male">Male</option>
                                    <option value="female">Female</option>
                                    <option value="transgender">Transgender</option>
                                    <option value="other">Do not identify as male, female, or transgender</option>
                                    <option value="n/a">Prefer not to say</option>
                                </select>
                            </div>
                            <div className="d-flex justify-content-center mt-4 mb-1">
                                <button 
                                    id="submit" 
                                    className="btn btn-primary submit sf-pro-bold w-100" 
                                    type="submit">
                                    SIGN UP
                                </button>
                            </div>
                            { 
                                accountCreateStatus == 1 ? <p className="successMessage move-medium text-center">Account Created!</p> : 
                                accountCreateStatus == 2 ? <p className="failMessage move-medium text-center">Account Creation Failed!</p> : null 
                            }
                        </div>
                    </form>
                </div>
            </div>
        </div>
    );
}
  /*
    <select id="q5" onChange={answerClicked} className="input-box form-select flex-styling-33" required>
        <option disabled value>Select</option>
        <option value="male">Male</option>
        <option value="female">Female</option>
    </select>
  */
export default CreateAccount