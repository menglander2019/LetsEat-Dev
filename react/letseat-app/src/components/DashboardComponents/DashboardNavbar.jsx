import React, { Component } from 'react'
import { Link, useNavigate } from 'react-router-dom'

import { IconContext } from 'react-icons'
import * as FaIcons from 'react-icons/fa'
import * as AiIcons from 'react-icons/ai'
import * as BoxIcons from 'react-icons/bi'
import * as BsIcons from "react-icons/bs"
import * as Ionicons from "react-icons/io";
import * as Heroicons from "react-icons/hi";


import logoPath from "../../design-resources/logo/letseat-banner-white.png"

// Takes in JSON data of a restaurant and parses the data
const DashboardNavbar = () => {
    const navigate = useNavigate()

    const logOut = async (e) => {
        e.preventDefault()
        const requestOption = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            credentials: "include"
        }

        const response = await fetch("http://ec2-100-24-238-253.compute-1.amazonaws.com:8000/logout", requestOption)
        //const data = await response.json()
        localStorage.removeItem("token")
        navigate("/")
    } 

    return (
        <div className="home-navbar-white">
            <div className="navbar align-items-center padding-style-1">
                <div className="d-flex justify-content-start">
                    <Link to="/dashboard">
                        <img src={logoPath} className="letseat-logo-navbar" />
                    </Link>
                </div>
                <div className="col-md-4">
                    <div className="d-flex flex-wrap justify-content-between align-items-center">
                            <Link to="/dashboard/">  
                                <span className="move-medium white-theme">Dashboard</span>
                            </Link>
                            <Link to="/group/">  
                                <span className="move-medium white-theme">Group</span>
                            </Link>
                            <Link to="/edit/preferences/">  
                                <span className="move-medium white-theme">Profile</span>
                            </Link>
                            <Link to="/">
                                <button onClick={logOut} className="btn navbar-signup-white-v2">
                                    <span className="move-medium">Sign Out</span>
                                </button>
                            </Link>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default DashboardNavbar