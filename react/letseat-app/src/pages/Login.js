import React, { Component } from 'react'
import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'

import HomeNavbar from '../components/HomeComponents/HomeNavbar';


function CreateAccount() {

    const handleSubmitButton = () => {
        alert("Log In!")
    }

    return (
        <>
        <div className="container-fluid">
            <HomeNavbar />
            <div className="d-flex align-items-center justify-content-center h-100">
                <div className="col-md-3">
                    <div className="d-flex flex-column">
                        <div className="row mt-4">
                            <h3 className="colfax-regular">Welcome to LetsEat!</h3>
                        </div>
                        <div className="row mt-2">
                            <div className="col-md-12">
                                <label for="email">Log In</label>
                                <input type="text" id="email" className="login-box form-control w-100 mt-3" placeholder="Enter email"></input>
                                <input type="text" id="password" className="login-box form-control w-100 mt-3" placeholder="Enter password"></input>
                            </div>
                        </div>
                        <div className="row mt-4">
                            <div className="col-md-12">
                                <button 
                                    id="submit"
                                    className="btn btn-primary submit w-100"
                                    onClick={handleSubmitButton}>
                                    Log In
                                </button>
                            </div>
                        </div>
                        <div className="row mt-4">
                            <div className="col-md-12">
                                <p className="colfax-regular">
                                    Don't have an account?
                                    <Link to="/createaccount">
                                        <span>Sign Up</span>
                                    </Link>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        </>
    );
}
  

export default CreateAccount