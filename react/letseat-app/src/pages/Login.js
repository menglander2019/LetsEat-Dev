import React, { Component } from 'react'
import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'

function CreateAccount() {

    const handleSubmitButton = () => {
        alert("Log In!")
    }

    return (
        <div className="container">
            <div className="col-md-4 mt-4 login-container mx-auto">
                <div className="row mt-4">
                    <div className="col-md-12 mx-auto">
                        <h3>Welcome to LetsEat!</h3>
                    </div>
                </div>
                <div className="row mt-2">
                    <div className="col-md-12 mx-auto">
                        <label for="email">Log In</label>
                        <input type="text" id="email" className="login-box form-control w-100 mt-3" placeholder="Enter email"></input>
                        <input type="text" id="password" className="login-box form-control w-100 mt-3" placeholder="Enter password"></input>
                    </div>
                </div>
                <div className="row mt-4">
                    <div className="col-md-12 mx-auto">
                        <button 
                            id="submit"
                            className="btn btn-primary submit w-100"
                            onClick={handleSubmitButton}>
                            Log In
                        </button>
                    </div>
                </div>
                <div className="row mt-4">
                    <div className="col-md-12 mx-auto">
                        <p>
                            Don't have an account?
                            <Link to="/createaccount">
                                <span>Sign Up</span>
                            </Link>
                        </p>
                    </div>
                </div>
            </div>
        </div>
    );
}
  

export default CreateAccount