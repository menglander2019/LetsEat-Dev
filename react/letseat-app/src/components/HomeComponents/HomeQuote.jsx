import React, { Component } from 'react'
import { Link } from 'react-router-dom'

// Takes in JSON data of a restaurant and parses the data
const HomeQuote = () => {

    return (
        <div className="home-quote d-flex align-items-center justify-content-center">
            <div className="big-quote padding-style-6">
                <p className="white-theme move-bold font-size-sm-3 text-center">"LetsEat provides personalized restaurant recommendations using a unique machine learning algorithm"</p>
            </div>
        </div>
    )
}

export default HomeQuote