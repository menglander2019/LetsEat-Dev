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
                            <h2>LetsEat</h2>
                        </div>
                        <div class="d-flex justify-content-end">
                            <Link to="/login">
                                <button className="btn navbar-login">
                                    <span>Log In</span>
                                </button>
                            </Link>
                            <Link to="/createaccount">
                                <button className="btn navbar-signup">
                                    <span>Sign Up</span>
                                </button>
                            </Link>
                        </div>
                    </div>
                    <div className="d-flex align-items-center justify-content-center">
                        <div className="col-md-6 mt-5">
                            <div className="home-main-block">
                                <div className="d-flex flex-column">
                                    <p className="display-5 text-center">Discover your new favorite restaurant nearby</p>
                                    <div className="d-flex justify-content-center">
                                        <p className="text-center flex-styling-75">
                                            Our machine learning powered algorithm will help you find new restaurants that match your unique preferences
                                        </p>
                                    </div>
                                    <div className="d-flex justify-content-center mt-4">
                                        <Link to="/login" className="flex-styling-33">
                                            <button 
                                                id="submit"
                                                className="btn home-large-login w-100">
                                                Get Started
                                            </button>
                                        </Link>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <hr />
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