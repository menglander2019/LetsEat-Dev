import React, { Component } from 'react'
import { Link } from 'react-router-dom'

// Takes in JSON data of a restaurant and parses the data
const HomeBanner = () => {

    return (
        <div className="home-banner">
            <div className="d-flex align-items-center justify-content-center">
                <div className="col-md-10">
                    <div className="home-main-block">
                        <div className="d-flex flex-column">
                            <p className="font-size-banner yellow-theme druk-bold">DISCOVER RESTAURANTS</p>
                            <div className="d-flex justify-content-start mt-1">
                                <Link to="/login" className="flex-styling-33">
                                    <button 
                                        id="submit"
                                        className="btn home-large-login sf-pro-bold w-100">
                                        DISCOVER NOW
                                    </button>
                                </Link>
                            </div>
                            <div className="d-flex justify-content-center">
                                <div class="lds-ellipsis"><div></div><div></div><div></div><div></div></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default HomeBanner