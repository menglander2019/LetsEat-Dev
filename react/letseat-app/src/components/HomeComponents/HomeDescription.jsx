import React, { Component } from 'react'

// Takes in JSON data of a restaurant and parses the data
const HomeDescription = () => {
 
    return (
        <>
            <hr />
            <div className="home-description padding-style-1">
                <div className="d-flex flex-wrap align-items-start">
                    <div className="col-md-6">
                        <div className="d-flex justify-content-start">
                            <h2 className="text-center charter-regular">What is LetsEat?</h2>
                        </div>
                    </div>
                    <div className="col-md-6">
                        <div className="d-flex justify-content-start">
                            <p className="colfax-regular">
                                LetsEat is a restaurant cuisine recommendation website that provides users with personalized recommendations for where to eat based on their preferences. 
                                Our platform works by using a machine learning algorithm to match users with restaurants that have been liked by other users with similar preferences.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}

export default HomeDescription