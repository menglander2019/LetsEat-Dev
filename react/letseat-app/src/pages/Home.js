import React, { Component } from 'react'
import { useEffect, useState } from 'react'
import { Link, Navigate } from 'react-router-dom'
import 'bootstrap/dist/css/bootstrap.css'

import HomeDescription from '../components/HomeComponents/HomeDescription';
import HomeBanner from '../components/HomeComponents/HomeBanner';
import HomeNavbar from '../components/HomeComponents/HomeNavbar';
import DashboardNavbar from '../components/DashboardComponents/DashboardNavbar';

import '../css/Animation.css';
import '../css/Button.css';
import '../css/Color.css';
import '../css/Font.css';
import '../css/Home.css';
import '../css/Padding.css';
import '../css/Navbar.css'

function Home() {

    return (
        <div className="container-fluid">
            <div className="background-image-banner">
                <div className="d-flex flex-column">
                    {
                        localStorage.getItem("token") == null ? <HomeNavbar /> : <DashboardNavbar />
                    }
                    <HomeBanner />
                    <HomeDescription />
                </div>
            </div>
        </div>
    );
}
  

export default Home