import React, { Component } from 'react'
import { Link } from 'react-router-dom'

// Takes in JSON data of a restaurant and parses the data
const HomeBanner = () => {

    return (
        <div className="home-banner">
            <div className="d-flex align-items-center justify-content-center">
                <div className="col-md-6 mt-5">
                    <div className="home-main-block">
                        <div className="d-flex flex-column">
                            <p className="display-4 text-center charter-regular">Discover your new favorite restaurant nearby.</p>
                            <div className="d-flex justify-content-center mt-3">
                                <p className="text-center font-size-md colfax-regular flex-styling-75">
                                    Our machine learning powered algorithm will help you find new restaurants that match your unique preferences. 
                                </p>
                            </div>
                            <div className="d-flex justify-content-center mt-4">
                                <Link to="/login" className="flex-styling-33">
                                    <button 
                                        id="submit"
                                        className="btn home-large-login colfax-regular w-100">
                                        Alpha Prototype
                                    </button>
                                </Link>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default HomeBanner