import React, { Component } from 'react'
import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom';

import TestData from '../data/test-data.json'
import RestaurantCard from '../components/RestaurantCard'
import DashboardNavbar from '../components/DashboardComponents/DashboardNavbar';
import LoadingAnimation from '../components/LoadingAnimation';

import '../css/Restaurant.css';

import url from '../WebsiteURL'

function NoResults() {

    const navigate = useNavigate()

    const backButton = () => {
        navigate("/dashboard")
    }

    return (
        <div className="container-fluid restaurant-component">
            <DashboardNavbar />
            <div className="d-flex justify-content-center h-100">
                <div className="col-md-6 mt-5">
                    <div className="restaurant-main-block">
                        <div className="d-flex flex-column">
                            <h1 className="move-medium text-center mt-2">Sorry, we're out of results!</h1>
                            <p className="move-medium black-theme text-center mt-2">We are always trying to improve LetsEat to give you the best recommendations. Try editing your preferences to receive more results</p>
                            <div className="d-flex justify-content-center mt-2">
                                <div className="flex-styling-33">
                                    <button 
                                        id="submit"
                                        className="btn search-navigation move-medium w-100"
                                        onClick={backButton}>
                                        Back
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}
  

export default NoResults