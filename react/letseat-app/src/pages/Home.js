import React, { Component } from 'react'
import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import 'bootstrap/dist/css/bootstrap.css'
import '../css/Home.css';

function Home() {
    return (
        <div className="container">
            <div className="col-md-8 mt-4 mx-auto">
                <div className="row mt-3">
                    <div className="col">
                        <h1 className="display-3 text-center">LetsEat</h1>
                    </div>
                </div>
                <div className="row">
                    <div className="col">
                        <h2 className="text-center">Explore new restaurants near you.</h2>
                    </div>
                </div>
                <div>
                    <Link to="/createaccount">
                        <span>Create Account</span>
                    </Link><br />
                    <Link to="/createprofile">
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