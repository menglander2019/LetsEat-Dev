import React, { Component } from 'react'
import { Link } from 'react-router-dom'

// Takes in JSON data of a restaurant and parses the data
const HomeDescription = () => {
 
    return (
        <>
            <div className="home-description padding-style-4">
                <div className="d-flex flex-wrap align-items-start">
                    <div className="col-md-7">
                        <div className="d-flex flex-column justify-content-start">
                            <h2 className="black-theme move-bold">We match your preferences and restrictions to restaurants for you</h2>
                            <p className="font-size-sm black-theme move-medium mt-4">
                                Free to use platform that saves you time deciding on where <br /> to eat next by yourself or with a group.
                            </p>
                            <div className="mt-1">
                            <Link to="/login">
                                <button className="btn home-description-button">
                                    <span className="move-bold">Try it now</span>
                                </button>
                            </Link>
                            </div>
                        </div>

                    </div>
                    <div className="col-md-5">
                        <div className="home-image-description"></div>
                    </div>
                </div>
            </div>
        </>
    )
}

export default HomeDescription