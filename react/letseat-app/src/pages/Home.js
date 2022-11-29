import React, { Component } from 'react'
import { useEffect, useState } from 'react'
import { Link, Navigate } from 'react-router-dom'
import 'bootstrap/dist/css/bootstrap.css'
import '../css/Home.css';

import HomeDescription from '../components/HomeComponents/HomeDescription';
import HomeBanner from '../components/HomeComponents/HomeBanner';
import HomeNavbar from '../components/HomeComponents/HomeNavbar';
import DashboardNavbar from '../components/DashboardComponents/DashboardNavbar';

function Home() {

    return (
        <div className="container-fluid">
            <div className="d-flex flex-column">
                {
                    localStorage.getItem("token") == null ? <HomeNavbar /> : <DashboardNavbar />
                }
                <HomeBanner />
                <HomeDescription />
            </div>
        </div>
    );
}
  

export default Home