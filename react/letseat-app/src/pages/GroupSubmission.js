import React, { Component } from 'react'
import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom';

import TestData from '../data/test-data.json'
import RestaurantCard from '../components/RestaurantCard'
import DashboardNavbar from '../components/DashboardComponents/DashboardNavbar';
import LoadingAnimation from '../components/LoadingAnimation';

import '../css/Restaurant.css';

import url from '../WebsiteURL'

function GroupSubmission() {

    const navigate = useNavigate()

    const backButton = () => {
        navigate("/dashboard")
    }

    return (
        <div className="container-fluid group-profile-component">
                <div className="d-flex flex-column">
                    <div className="d-flex align-items-center justify-content-center">
                        <div className="col-md-6 mt-5">
                            <div className="profile-main-block">
                                <h1 className="text-center move-medium black-theme">Group Submission Successful!</h1>
                            </div>
                        </div>
                    </div>
                </div>
            </div> 
    );
}
  

export default GroupSubmission