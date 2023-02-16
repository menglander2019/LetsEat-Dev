import React, { Component } from 'react'
import { Link } from 'react-router-dom'

// Takes in JSON data of a restaurant and parses the data
const NewHomeBanner = () => {

    return (
        <div className="new-home-banner">
            <div className="d-flex flex-wrap">
                <div className="col-md-6 card-banner">
                    <div className="home-main-block padding-style-5">
                        <h2 className="white-theme move-bold">Discover your new favorite restaurants.</h2>
                        <br /><br /><br /><br /><br /><br />
                        <Link to="/login">
                            <h4 className="white-theme move-bold ">Discover Now {' >'}</h4>
                        </Link>
                    </div>
                </div>
                <div className="col-md-6">
                    <div className="home-image-banner"></div>
                </div>
            </div>
        </div>
    )
}

export default NewHomeBanner