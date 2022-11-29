import React, { Component } from 'react'
import { Link } from 'react-router-dom'

// Takes in JSON data of a restaurant and parses the data
const HomeBanner = () => {

    return (
        <div className="home-banner">
            <div className="d-flex align-items-center justify-content-center">
                <div className="col-md-6">
                    <div className="home-main-block">
                        <div className="d-flex flex-column">
                            <div className="d-flex justify-content-center">
                                <div class="lds-ellipsis"><div></div><div></div><div></div><div></div></div>
                            </div>
                            <p className="font-size-md text-center charter-regular">Discover your new favorite restaurant nearby.</p>
                            <div className="d-flex justify-content-center mt-1">
                                <p className="text-center colfax-regular font-size-sm flex-styling-75">
                                    Our machine learning powered algorithm will help you find new restaurants that match your unique preferences. 
                                </p>
                            </div>
                            <div className="d-flex justify-content-center mt-3">
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