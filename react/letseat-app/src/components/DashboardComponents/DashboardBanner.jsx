import React, { Component } from 'react'
import { Link } from 'react-router-dom'

// Takes in JSON data of a restaurant and parses the data
const DashboardBanner = () => {

    const searchButtonClicked = async (e) => {
        e.preventDefault()
        const response = await fetch("http://127.0.0.1:8000/isNewUser/")
        const message = await response.json()
        console.log(message)
    }

    return (
        <div className="home-banner">
            <div className="d-flex align-items-center justify-content-center">
                <div className="col-md-6 mt-5">
                    <div className="home-main-block">
                        <div className="d-flex flex-column">
                            <p className="display-4 text-center charter-regular">Begin your search.</p>
                            <div className="d-flex justify-content-center mt-3">
                                <p className="text-center font-size-md colfax-regular">
                                    Answer the questionnaire to generate your recommendations.
                                </p>
                            </div>
                            <div className="d-flex justify-content-center mt-4">
                                <div className="flex-styling-33">
                                    <button 
                                        id="submit"
                                        className="btn home-large-login colfax-regular w-100"
                                        onClick={searchButtonClicked}>
                                        Search
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default DashboardBanner