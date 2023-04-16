import React, { Component } from 'react'
import { Link } from 'react-router-dom'

import logoPath from "../design-resources/logo/letseat-banner-white.png"

// Takes in JSON data of a restaurant and parses the data

const LogoNavbar = () => {

    return (
        <div className="home-navbar-black">
            <div className="navbar align-items-center padding-style-3">
                <div class="d-flex justify-content-start">
                    <img src={logoPath} className="letseat-logo-navbar" />
                </div>
            </div>
        </div>
    )
}

export default LogoNavbar