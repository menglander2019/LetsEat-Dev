import React, { Component } from 'react'
import { Link } from 'react-router-dom'

// Takes in JSON data of a restaurant and parses the data
const DashboardBanner = ({searchFunction}) => {

    return (
        <div className="home-banner">
            <div className="d-flex align-items-center justify-content-center">
                <div className="col-md-6 mt-5">
                    <div className="home-main-block">
                        <div className="d-flex flex-column">
                            <div className="d-flex justify-content-center">
                                <div class="lds-ellipsis"><div></div><div></div><div></div><div></div></div>
                            </div>
                            <p className="font-size-md text-center charter-regular">Welcome Back.</p>
                            <div className="d-flex justify-content-center mt-1">
                                <p className="text-center font-size-sm colfax-regular">
                                    Answer the questionnaire to generate your recommendations.
                                </p>
                            </div>
                            <div className="d-flex justify-content-center mt-2">
                                <div className="flex-styling-33">
                                    <button 
                                        id="submit"
                                        className="btn home-large-login colfax-regular w-100"
                                        onClick={searchFunction}>
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