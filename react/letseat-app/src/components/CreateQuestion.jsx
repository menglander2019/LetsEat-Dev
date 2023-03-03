import React from 'react'

import ButtonCreate from '../components/ButtonCreate'


const CreateQuestion = ({ question, questionNumber, radioAnswerClicked, flexStylingOption }) => {
  
  const questionNumberDisplay = questionNumber + 1
  const divNumber = "q" + questionNumberDisplay
  return (
    <div id={divNumber} className="question mt-3" onClick={radioAnswerClicked}>
      <label for="answerOptions">{question.question}</label>
      <ButtonCreate answerOptions={question.answerChoices} questionNumber={"q1"} optionType={flexStylingOption} />
    </div>
  )
}

export default CreateQuestion