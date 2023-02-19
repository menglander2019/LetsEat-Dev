import React, { Component } from 'react'
import { Link, useNavigate } from 'react-router-dom'

import { IconContext } from 'react-icons'
import * as FaIcons from 'react-icons/fa'
import * as AiIcons from 'react-icons/ai'
import * as BoxIcons from 'react-icons/bi'
import * as BsIcons from "react-icons/bs"
import * as IconName from "react-icons/io";

import logoPath from "../../design-resources/logo/letseat-banner.png"

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

        const response = await fetch("http://localhost:8000/logout", requestOption)
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
                <div className="d-flex justify-content-end">
                    <div className="d-flex flex-wrap align-items-center justify-content-between">
                        <Link to="/edit/preferences/">  
                            <IconContext.Provider value={{ color: "black", size: 25 }}>
                                <button className="btn">
                                    <FaIcons.FaUser />
                                </button>
                            </IconContext.Provider>
                        </Link>
                        <Link to="/">
                            <button onClick={logOut} className="btn navbar-signup-black">
                                <span className="move-bold">Sign Out</span>
                            </button>
                        </Link>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default DashboardNavbar