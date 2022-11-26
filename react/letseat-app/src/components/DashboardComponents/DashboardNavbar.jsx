import React, { Component } from 'react'
import { Link, useNavigate } from 'react-router-dom'

// Takes in JSON data of a restaurant and parses the data
const DashboardNavbar = () => {
    const navigate = useNavigate()

    const logOut = () => {
        localStorage.removeItem("token")
        navigate("/")
    }

    return (
        <div className="home-navbar">
            <div className="navbar align-items-center padding-style-1">
                <div class="d-flex justify-content-start">
                    <Link to="/">
                        <h2 className="charter-regular">
                            LetsEat
                        </h2>
                    </Link>
                </div>
                <div class="d-flex justify-content-end">
                    <Link to="/">
                        <button onClick={logOut} className="btn navbar-signup">
                            <span>Log Out</span>
                        </button>
                    </Link>
                </div>
            </div>
        </div>
    )
}

export default DashboardNavbar