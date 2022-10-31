import React, { Component } from 'react'

// Takes in JSON data of a restaurant and parses the data
const PreviousNextButton = ({ questionIndex, previousQuestion, nextQuestion, numQuestions }) => {

    return (
        <div className="previousNextButton">
            {   questionIndex > 0 
                ? (
                    <button id="previousButton" onClick={previousQuestion}>Previous</button>
                ) :
                (
                    null
                )
            }
            {   questionIndex < numQuestions - 1 
                ? (
                    <button id="nextButton" onClick={nextQuestion}>Next</button>
                ) :
                (
                    null
                )
            }
        </div>
    )
}

export default PreviousNextButton