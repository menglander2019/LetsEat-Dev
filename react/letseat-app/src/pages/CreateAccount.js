import React, { Component } from 'react'
import { useEffect, useState } from 'react'

function CreateAccount() {

    const handleSubmitButton = () => {
        alert("Account Create!")
    }

    return (
        <div className="container">
            <div className="d-flex align-items-center justify-content-center h-100">
                <div className="col-md-5 mt-4">
                    <div className="d-flex flex-column">
                        <h1 className="display-3 text-center">LetsEat</h1>
                        <h3 className="mt-3 text-center">Sign up for free to find your new favorite restaurant.</h3>
                        <div className="question mt-3">
                            <label for="email">Enter your email</label>
                            <input type="text" id="email" className="input-box form-control w-100" placeholder="Enter an email"></input>
                            <small id="nameHelp" className="form-text text-muted">We'll never share your email with anyone else.</small>
                        </div>
                        <div className="question mt-3">
                            <label for="password">Create a password</label>
                            <input type="text" id="password" className="input-box  form-control w-100" placeholder="Create a password"></input>
                        </div>
                        <div className="question mt-3">
                            <label for="name">What should we call you?</label>
                            <input type="text" id="name" className="input-box form-control w-100" placeholder="Enter a profile name"></input>
                            <small id="profileNameHelp" className="form-text text-muted">We recommend using your first name.</small>
                        </div>
                        <div className="question mt-3">
                            <label>Enter your date of birth</label>
                            <div className="d-flex flex-row justify-content-between">
                                <select id="month" className="input-box form-select flex-styling-33">
                                    <option selected disabled value>Month</option>
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
                                <input type="text" id="day" className="input-box form-control flex-styling-33" maxLength="2" inputMode="numeric" placeholder="DD"></input>
                                <input type="text" id="year" className="input-box form-control flex-styling-33" maxLength="4" inputMode="numeric" placeholder="YYYY"></input>
                            </div>
                        </div>
                        <div className="question mt-3">
                            <label>What is your gender?</label>
                        </div>
                        <div className="question mt-4 mb-5">
                            <div className="d-flex flex-row justify-content-center">                            
                                <button 
                                    id="submit"
                                    className="btn btn-primary submit w-50"
                                    onClick={handleSubmitButton}>
                                    Sign Up
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}
  

export default CreateAccount