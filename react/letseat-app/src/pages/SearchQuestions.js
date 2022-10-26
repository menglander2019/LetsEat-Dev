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

    const [ questionIndex, setQuestionIndex ] = useState(0)
    const [ answerSelect, setAnswerSelect ] = useState("")

    const nextQuestion = () => {
        setQuestionIndex((questionIndex) => questionIndex + 1)
    }

    const previousQuestion = () => {
        setQuestionIndex((questionIndex) => questionIndex - 1)
    }

    const handleAnswerClick = (e) => {
        alert(e.target.getAttribute("questionNumber"))
    }

    const handleSubmitButton = () => {
        alert("Search Create!")
    }

    return (
        <div className="container">
            <div className="col-md-7 mt-4 mx-auto">
                <h1 className="display-3">Search Questions</h1>
                <div id="searchQuestions">
                    <div className="row mt-3">
                        <div className="question">
                            <label for="answerOptions">What is the occasion?</label>
                            <ButtonCreate answerOptions={questionBank[0].answers} questionNumber={0} colNumber={6} onClickFunction={handleAnswerClick} />
                        </div>
                    </div>
                    <div className="row mt-3">
                        <div className="question">
                            <label for="answerOptions">How many people?</label>
                            <ButtonCreate answerOptions={questionBank[1].answers} questionNumber={1} colNumber={6} onClickFunction={handleAnswerClick} />
                        </div>
                    </div>
                    <div className="row mt-3">
                        <div className="question">
                            <label for="answerOptions">What type of meal?</label>
                            <ButtonCreate answerOptions={questionBank[2].answers} questionNumber={2} colNumber={6} onClickFunction={handleAnswerClick} />
                        </div>
                    </div>
                    <div className="row mt-3">
                        <div className="question">
                            <label for="answerOptions">What is the price range?</label>
                            <ButtonCreate answerOptions={questionBank[3].answers} questionNumber={3} colNumber={6} onClickFunction={handleAnswerClick} />
                        </div>
                    </div>
                    <div className="row mt-3">
                        <div className="question">
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
                                    onClick={handleSubmitButton}>
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