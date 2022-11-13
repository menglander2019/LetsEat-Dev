import React, { Component } from 'react'
import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import 'bootstrap/dist/css/bootstrap.css'
import '../css/Home.css';

function Home() {
    return (
        <div className="container-fluid">
            <div className="home-banner">
                <div className="col-md-12">
                    <div className="row">
                        <div className="col-md-8">
                            <h2 className="white-theme">LetsEat</h2>
                        </div>
                    </div>
                    <div className="row mt-5">
                        <div className="col-md-6 mx-auto">
                            <h1 className="display-3 white-theme text-center">Discover your new favorite restaurant</h1>
                        </div>
                    </div>
                    <div className="row mt-4">
                        <div className="col-md-4 mx-auto">
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
    );
}
  

export default Home