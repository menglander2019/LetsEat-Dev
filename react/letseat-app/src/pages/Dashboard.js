import React, { Component } from 'react'
import { useEffect, useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import 'bootstrap/dist/css/bootstrap.css'

import HomeBanner from '../components/HomeComponents/HomeBanner';
import DashboardBanner from '../components/DashboardComponents/DashboardBanner';
import DashboardNavbar from '../components/DashboardComponents/DashboardNavbar';

import '../css/Animation.css';
import '../css/Button.css';
import '../css/Color.css';
import '../css/Font.css';
import '../css/Home.css';
import '../css/Padding.css';
import '../css/Dashboard.css';

function Dashboard() {
    const navigate = useNavigate()

    useEffect(() => {
        checkCredentials()
    }, [])

    // Checks user credentials
    const checkCredentials = async () => {
        if (localStorage.getItem("token") == null) {
            navigate("/")
        }
    }

    const searchButtonClicked = async (e) => {
        e.preventDefault()
        navigate("/searchquestions")
    }

    return (
        <div className="container-fluid dashboard-component">
            <div className="d-flex flex-column">
                <DashboardNavbar />
                <DashboardBanner searchFunction={searchButtonClicked}/>
            </div>
        </div>
    );
}
  

export default Dashboard