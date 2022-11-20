import React, { Component } from 'react'
import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import 'bootstrap/dist/css/bootstrap.css'
import '../css/Home.css';

function Home() {
    return (
        <div className="container-fluid">
            <div className="d-flex flex-column">
                <div className="home-banner">
                    <div className="navbar padding-style-1">
                        <div class="d-flex justify-content-start">
                            <h2 className="white-theme">LetsEat</h2>
                        </div>
                        <div class="d-flex justify-content-end">
                            <Link to="/login">
                                <button className="btn btn-primary navbar-login">
                                    <span>Log In</span>
                                </button>
                            </Link>
                            <Link to="/createaccount">
                                <button className="btn btn-primary navbar-signup">
                                    <span>Sign Up</span>
                                </button>
                            </Link>
                        </div>
                    </div>
                    <div className="d-flex flex-row justify-content-center mt-5">
                        <div className="col-md-8">
                            <h1 className="display-3 white-theme text-center">Discover your new favorite restaurant</h1>
                        </div>
                    </div>
                    <div className="d-flex flex-row justify-content-center mt-4">
                        <div className="col-md-4">
                            <Link to="/login">
                                <button 
                                    id="submit"
                                    className="btn btn-primary home-large-login w-100">
                                    Get Started
                                </button>
                            </Link>
                        </div>
                    </div>
                </div>
                <div className="home-description padding-style-1 mt-3">
                    <h2>What is LetsEat?</h2>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
                </div>
                <div className="row mt-5">
                    <Link to="/login">
                        <span>Login</span>
                    </Link><br />
                    <Link to="/createaccount">
                        <span>Create Account</span>
                    </Link><br />
                    <Link to="/edit/account">
                        <span>Edit Account</span>
                    </Link><br />
                    <Link to="/edit/preferences">
                        <span>Profile Questions</span>
                    </Link><br />
                    <Link to="/searchquestions">
                        <span>Search Questions</span>
                    </Link><br />
                    <Link to="/restaurantsearch">
                        <span>Restaurant</span>
                    </Link>
                </div>
            </div>
        </div>
    );
}
  

export default Home