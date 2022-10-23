import React, { Component } from 'react'
import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'

function CreateAccount() {

    const handleSubmitButton = () => {
        alert("Account Create!")
    }

    return (
        <div className="container">
            <div className="col-md-5 mt-4 mx-auto">
                <div className="row mt-3">
                    <div className="col-md-12 mx-auto">
                        <h3 className="mt-3">Welcome to LetsEat</h3>
                        <label for="email">Email</label>
                        <input type="text" id="email" className="login-box form-control w-100" placeholder="Enter your email"></input>
                    </div>
                </div>
                <div className="row mt-3">
                    <div className="col-md-12 mx-auto">
                        <label for="password">Password</label>
                        <input type="text" id="password" className="login-box  form-control w-100" placeholder="Create a password"></input>
                    </div>
                </div>
                <div className="row mt-4 mb-5">
                    <div className="col-md-12 mx-auto">
                        <button 
                            id="submit"
                            className="btn btn-primary submit w-100"
                            onClick={handleSubmitButton}>
                            Log In
                        </button>
                    </div>
                </div>
                <div className="row mt-3">
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