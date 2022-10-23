import React, { Component } from 'react'
import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'

function CreateAccount() {

    const handleSubmitButton = () => {
        alert("Log In!")
    }

    return (
        <div className="container">
            <div className="col-md-5 mt-4 mx-auto">
                <div className="row">
                    <div className="col-md-12 mx-auto">
                        <h3>Account Preferences</h3>
                    </div>
                </div>
                <div className="row mt-3">
                    <div className="col-md-12 mx-auto">
                        <label for="email">Update Your Email Address (Populate with user email)</label>
                        <input type="text" id="email" className="login-box form-control w-100" placeholder="Enter your email"></input>
                    </div>
                </div>
                <div className="row mt-3">
                    <div className="col-md-12 mx-auto">
                        <label for="email">Update Your Name(Populate with user name)</label>
                        <input type="text" id="email" className="login-box form-control w-100" placeholder="Enter your new username"></input>
                    </div>
                </div>
                <div className="row mt-3">
                    <div className="col-md-12 mx-auto">
                        <label for="password">Update Your Password</label>
                        <input type="text" id="password" className="login-box form-control w-100" placeholder="Enter your new password"></input>
                        <input type="text" id="password" className="login-box form-control w-100" placeholder="Retype your new password"></input>
                    </div>
                </div>
                <div className="row mt-4">
                    <div className="col-md-12 mx-auto">
                        <button 
                            id="submit"
                            className="btn btn-primary submit w-100"
                            onClick={handleSubmitButton}>
                            Update Preferences
                        </button>
                    </div>
                </div>
            </div>
        </div>
    );
}
  

export default CreateAccount