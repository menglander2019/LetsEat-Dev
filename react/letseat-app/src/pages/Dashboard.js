import React, { Component } from 'react'
import { useEffect, useState } from 'react'
import { Link, Navigate } from 'react-router-dom'
import 'bootstrap/dist/css/bootstrap.css'
import '../css/Home.css';

import HomeBanner from '../components/HomeComponents/HomeBanner';
import DashboardBanner from '../components/DashboardComponents/DashboardBanner';
import DashboardNavbar from '../components/DashboardComponents/DashboardNavbar';

function Dashboard() {
    if (localStorage.getItem("token") == null) {
        return ( <Navigate to="/" /> )
    } else {
        return (
            <div className="container-fluid">
                <div className="d-flex flex-column">
                    <DashboardNavbar />
                    <DashboardBanner />
                </div>
            </div>
        );
    }
}
  

export default Dashboard