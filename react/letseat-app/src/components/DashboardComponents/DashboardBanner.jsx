import React, { Component } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { useEffect, useState } from 'react'

// Takes in JSON data of a restaurant and parses the data
const DashboardBanner = () => {

    const navigate = useNavigate()
    const [ groupCreated, setGroupCreated ] = useState(0)
    
    useEffect(() => {
        getGroupCreationStatus()
    }, [])

    const getGroupCreationStatus = async () => {
        const requestOption = {
            method: "GET",
            credentials: "include",
            headers: { "Content-Type": "application/json"}
        }

        const response = await fetch("http://localhost:8000/createdGroupStatus", requestOption)
            .then(async response => {
                const data = await response.json()
                if (response.ok) {
                    setGroupCreated(data.created_status)
                } else {
                    console.log("Error!")
                }
            })
            .catch(error => {
                console.log("Error!")
            })
    }
    
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
            <div className="d-flex">
                <div className="col-md-6">
                    <div className="d-flex justify-content-center">
                        <div className="col-md-8 padding-style-7">
                            <div className="d-flex flex-column">
                                <h3 className="move-medium black-theme">Begin your search for restaurants near you</h3> 
                                <p className="move-medium grey-theme">Discover thousands of new restaurants based on your preferences</p>
                                <button 
                                    id="submit"
                                    className="btn dashboard-large-login move-medium w-100 mt-2"
                                    onClick={searchButtonClicked}>
                                    Search {'>'}
                                </button>
                                {
                                        groupCreated != 0 ?
                                            <button 
                                                id="submit"
                                                className="btn dashboard-large-login move-medium w-100 mt-2"
                                                onClick={groupSearchButtonClicked}>
                                                Group Search {'>'}
                                            </button>
                                            :
                                            <button 
                                                id="submit"
                                                className="btn dashboard-large-login move-medium disabled w-100 mt-2"
                                                onClick={groupSearchButtonClicked}>
                                                Group Search {'>'}
                                            </button>

                                }
                                
                            </div>
                        </div>
                    </div>
                </div>
                <div className="col-md-6">
                    <div className="dashboard-image"></div>
                </div>
            </div>
        </div>
    )
}

export default DashboardBanner