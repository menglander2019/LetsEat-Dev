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

    return (
        <div className="container-fluid dashboard-component">
            <div className="d-flex flex-column">
                <div className="dashboard-banner">
                    <div className="d-flex">
                        <div className="col-md-6">
                            <div className="d-flex justify-content-center">
                                <div className="col-md-8 padding-style-7">
                                    <div className="d-flex flex-column">
                                    <h1 className="move-medium black-theme">Group Submission Successful!</h1>
                                    <p className="move-medium black-theme mt-3">Thank you for your submission. Your preferences will be added to the group search</p>
                                    <p className="move-medium grey-theme mt-3">You may now close this page.</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div className="col-md-6">
                            <div className="group-image"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}
  

export default GroupSubmission