import React, { Component } from 'react'
import { useEffect, useState } from 'react'

import * as FaIcons from 'react-icons/fa'
import * as AiIcons from 'react-icons/ai'
import * as BoxIcons from 'react-icons/bi'
import { IconContext } from 'react-icons'

import PreviousNextButton from '../components/PreviousNextButton'
import ButtonCreate from '../components/ButtonCreate'

function ProfileQuestions() {

    const [ questionIndex, setQuestionIndex ] = useState(0)

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
            // Remove Selection from Fast API
        } else {
            // Select Answer
            clickedChoice.classList.add("selected");
            // Send Selection to Fast API
        }
    }
    const handleSubmitButton = () => {
        alert("Profile Create!")
    }

    var cuisineChoices = ["American", "Mexican", "French", "Chinese", "Japanese", "Italian", "Korean", "Thai"]
    var allergyChoices = ["Gluten", "Eggs", "Dairy", "Peanuts"]
    var numQuestions = 3

    return (
        <div className="container">
            <div className="col-md-7 mt-4 mx-auto">
                <h1 className="display-3">Profile Questions</h1>
                <div id="profileQuestions">
                    <div className="row mt-3">
                        <div id="q1" className="question" onClick={answerClicked}>
                            <label for="answerOptions">What are your cuisine preferences?</label>
                            <ButtonCreate answerOptions={cuisineChoices} colNumber={4} />
                        </div>
                    </div>
                    <div className="row mt-3">
                        <div id="q2" className="question" onClick={answerClicked}>
                            <label for="answerOptions">Any food restrictions or allergies?</label>
                            <ButtonCreate answerOptions={allergyChoices} colNumber={4} />
                        </div>
                    </div>
                    <div className="row mt-3">
                        <div id="q3" className="question" onClick={answerClicked}>
                            <label for="answerOptions">What cuisine do you want not recommended?</label>
                            <ButtonCreate answerOptions={cuisineChoices} colNumber={4} />
                        </div>
                    </div>
                    <div className="row mt-4 mb-5">
                        <div className="col-md-12 mx-auto">
                            <IconContext.Provider value={{ color: "white", size: 15 }}>
                                <button 
                                    id="submit" 
                                    className="btn btn-primary submit w-100 inactive" 
                                    onClick={handleSubmitButton}>
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

/**
 * <div className="row">
        <PreviousNextButton 
            questionIndex={questionIndex} 
            previousQuestion={previousQuestion} 
            nextQuestion={nextQuestion}
            numQuestions={numQuestions}/>
    </div>
 */
  

export default ProfileQuestions