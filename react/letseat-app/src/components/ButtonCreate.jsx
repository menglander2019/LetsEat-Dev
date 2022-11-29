import React, { Component } from 'react'

import * as FaIcons from 'react-icons/fa'

// Takes array of answer options and onClick function to generate buttons
const ButtonCreate = ({ answerOptions, questionNumber, optionType }) => {
    
    let optionTypeText = optionType

    return (
        <div id="answerOptions" className="d-flex flex-row flex-wrap">
            {answerOptions.map((answerOption, index) => (
                <button 
                    id={questionNumber + "-" + index}
                    type="button" 
                    className={"btn answerOption w-100 " + optionTypeText}
                    key={answerOption}
                    value={answerOption}>
                    {answerOption}
                </button>

            ))}
        </div>
    )
}

// Removed: onClick={onClickFunction}>


export default ButtonCreate