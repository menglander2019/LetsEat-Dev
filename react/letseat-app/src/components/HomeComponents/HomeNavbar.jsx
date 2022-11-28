import React, { Component } from 'react'
import { Link } from 'react-router-dom'

import logoPath from "../../design-resources/logo/letseat-banner.png"

// Takes in JSON data of a restaurant and parses the data
const HomeNavbar = () => {

    return (
        <div className="home-navbar">
            <div className="navbar align-items-center padding-style-1">
                <div class="d-flex justify-content-start">
                    <Link to="/">
                        <img src={logoPath} className="letseat-logo-navbar" />
                    </Link>
                </div>
                <div class="d-flex justify-content-end">
                    <Link to="/login">
                        <button className="btn navbar-login">
                            <span>Log In</span>
                        </button>
                    </Link>
                    <Link to="/createaccount">
                        <button className="btn navbar-signup">
                            <span>Sign Up</span>
                        </button>
                    </Link>
                </div>
            </div>
        </div>
    )
}

export default HomeNavbar