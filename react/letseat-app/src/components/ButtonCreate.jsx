import React, { Component } from 'react'

import * as FaIcons from 'react-icons/fa'

// Takes array of answer options and onClick function to generate buttons
const ButtonCreate = ({ answerOptions, questionNumber, colNumber }) => {

    let colSize = "col-md-" + colNumber
    return (
        <div id="answerOptions" className="row">
            {answerOptions.map((answerOption, index) => (
                <div className={colSize} key={answerOption}>
                    <button 
                        id={questionNumber + "-" + index}
                        type="button" 
                        className="btn answerOption w-100"
                        value={answerOption}>
                        {answerOption}
                    </button>
                </div>
            ))}
        </div>
    )
}

// Removed: onClick={onClickFunction}>


export default ButtonCreate