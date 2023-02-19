import React, { Component } from 'react'
import { Link } from 'react-router-dom'

// Takes in JSON data of a restaurant and parses the data
const DashboardBanner = ({searchFunction}) => {

    return (
        <div className="dashboard-banner">
            <div className="d-flex align-items-center justify-content-center">
                <div className="col-md-6 mt-5">
                    <div className="dashboard-main-block">
                        <div className="d-flex flex-column">
                            <h2 className="color-theme font-size-lg move-bold">Welcome Back!</h2>
                            <h4 className="color-theme move-bold">Let's begin your search</h4>
                            <div className="d-flex mt-2">
                                <button 
                                    id="submit"
                                    className="btn dashboard-large-login move-bold w-50"
                                    onClick={searchFunction}>
                                    Search {'>'}
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