import React, { Component } from 'react'
import { Link } from 'react-router-dom'

// Takes in JSON data of a restaurant and parses the data
const HomeBanner = () => {

    return (
        <div className="home-banner">
            <div className="home-main-block padding-style-5">
                <h3 className="white-theme sf-pro-bold ">Discover your new favorite restaurants.</h3>
                <br /><br /><br /><br /><br /><br />
                <h3 className="white-theme sf-pro-bold ">Discover Now {' >'}</h3>
            </div>
            <div className="d-flex align-items-right justify-content-center">
                <div className="col-md-10">
                    <div className="home-image-banner"></div>
                </div>
            </div>
        </div>
    )
}

export default HomeBanner