import React, { Component } from 'react'

import * as FaIcons from 'react-icons/fa'

// Takes array of answer options and onClick function to generate buttons
const ButtonCreate = ({ answerOptions, questionNumber, onClickFunction, colNumber }) => {

    let colSize = "col-md-" + colNumber
    return (
        <div id="answerOptions" className="row">
            {answerOptions.map((answerOption) => (
                <div className={colSize} key={answerOption}>
                    <button 
                        type="button" 
                        className="btn answerOption w-100"
                        value={answerOption}
                        onClick={onClickFunction}>
                        {answerOption}
                    </button>
                </div>
            ))}
        </div>
    )
}

export default ButtonCreate