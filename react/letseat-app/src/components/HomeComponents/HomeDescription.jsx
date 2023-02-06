import React, { Component } from 'react'

// Takes in JSON data of a restaurant and parses the data
const HomeDescription = () => {
 
    return (
        <>
            <hr />
            <div className="home-description padding-style-3">
                <div className="d-flex flex-wrap align-items-start">
                    <div className="col-md-6">
                        <div className="d-flex justify-content-start">
                            <p className="white-theme sf-pro-bold">Our machine learning algorithm recommends restaurants based on personal preferences and restrictions.</p>
                        </div>
                    </div>
                    <div className="col-md-6">
                        <div className="d-flex justify-content-start">
                            <p className="font-size-sm white-theme sf-pro-regular">
                                LetsEat is a restaurant cuisine recommendation website that provides users with personalized recommendations for where to eat based on their preferences. 
                                Our platform works by using a machine learning algorithm to match users with restaurants that have been liked by other users with similar preferences.
                                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Dui vivamus arcu felis bibendum. Sem fringilla ut morbi tincidunt. Sit amet nulla facilisi morbi. Nunc sed blandit libero volutpat sed cras ornare arcu. Quis risus sed vulputate odio ut. Ultrices gravida dictum fusce ut placerat orci nulla pellentesque. A diam maecenas sed enim. Blandit turpis cursus in hac habitasse platea. Amet nisl suscipit adipiscing bibendum est ultricies integer quis. Id aliquet risus feugiat in ante metus dictum at tempor.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}

export default HomeDescription