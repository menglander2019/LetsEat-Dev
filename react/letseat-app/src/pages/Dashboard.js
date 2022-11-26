import React, { Component } from 'react'
import { useEffect, useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import 'bootstrap/dist/css/bootstrap.css'
import '../css/Home.css';

import HomeBanner from '../components/HomeComponents/HomeBanner';
import DashboardBanner from '../components/DashboardComponents/DashboardBanner';
import DashboardNavbar from '../components/DashboardComponents/DashboardNavbar';

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
        const response = await fetch("http://127.0.0.1:8000/isNewUser/", {
            method: "GET",
            headers: { "Content-Type": "application/json" },
        })
        const message = await response.json()
        console.log(message)
    }

    return (
        <div className="container-fluid">
            <div className="d-flex flex-column">
                <DashboardNavbar />
                <DashboardBanner searchFunction={searchButtonClicked}/>
            </div>
        </div>
    );
}
  

export default Dashboard