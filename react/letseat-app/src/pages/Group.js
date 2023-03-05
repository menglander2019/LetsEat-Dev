import React from 'react'
import { useParams } from 'react-router-dom'
import { useEffect, useState } from 'react'

import DashboardNavbar from '../components/DashboardComponents/DashboardNavbar';

import '../css/Group.css';

const Group = () => {

    const { host } = useParams()
    console.log(host)

    useEffect(() => {
    
    }, [])

    const createGroup = async () => {
        console.log("Fetching Host!")
        const requestOption = {
            method: "GET",
            credentials: "include",
            headers: { "Content-Type": "application/json"}
        }

        const response = await fetch("http://localhost:8000/getGroupHostName", requestOption)
            .then(async response => {
                const data = await response.json()
                if (response.ok) {
                    console.log(data)
                } else {
                    console.log(data)
                }
            })
            .catch(error => {
                console.log("Error!")
            })
    }

    return (
        <div className="container-fluid group-component">
            <DashboardNavbar />
            <div className="d-flex flex-column">
                    <div className="d-flex align-items-center justify-content-center">
                        <div className="col-md-6 mt-5">
                            <div className="group-main-block">
                                <div className="d-flex flex-column">
                                    <h1 className="move-bold">Group Settings</h1>
                                    <button 
                                        id="submit"
                                        className="btn dashboard-large-login move-medium w-50 mt-3"
                                        onClick={createGroup}>
                                        Create Group {'>'}
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
        </div>
    )
}

export default Group