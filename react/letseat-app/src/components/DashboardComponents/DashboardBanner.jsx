import React, { Component } from 'react'
import { Link, useNavigate } from 'react-router-dom'

// Takes in JSON data of a restaurant and parses the data
const DashboardBanner = () => {

    const navigate = useNavigate()
    
    const searchButtonClicked = async (e) => {
        e.preventDefault()
        navigate("/newsearchquestions")
    }

    const groupSearchButtonClicked = async (e) => {
        e.preventDefault()
        navigate("/group/searchquestions")
    }

    return (
        <div className="dashboard-banner">
            <div className="d-flex align-items-center justify-content-center">
                <div className="col-md-6 mt-5">
                    <div className="dashboard-main-block">
                        <div className="d-flex flex-column">
                            <p className="black-theme font-size-lg move-medium">Welcome Back!</p>
                            <div className="d-flex mt-3">
                                <button 
                                    id="submit"
                                    className="btn dashboard-large-login move-medium w-50"
                                    onClick={searchButtonClicked}>
                                    Search {'>'}
                                </button>
                                <button 
                                    id="submit"
                                    className="btn dashboard-large-login move-medium w-50"
                                    onClick={groupSearchButtonClicked}>
                                    Group Search {'>'}
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default DashboardBanner