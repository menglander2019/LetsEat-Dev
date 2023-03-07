import React from 'react'
import { useParams } from 'react-router-dom'
import { useEffect, useState } from 'react'

import DashboardNavbar from '../components/DashboardComponents/DashboardNavbar';

import '../css/Group.css';

const Group = () => {

    const [ groupCreationStatus, setGroupCreationStatus ] = useState(0)

    useEffect(() => {
        checkGroupCreation()
    }, [])

    // Checks if user has already created a group
    const checkGroupCreation = async () => {
        const requestOption = {
            method: "GET",
            credentials: "include",
            headers: { "Content-Type": "application/json"}
        }

        const response = await fetch("http://ec2-52-86-251-227.compute-1.amazonaws.com:8000/createdGroupStatus", requestOption)
            .then(async response => {
                const data = await response.json()
                if (response.ok) {
                    if (data.created_status == 0) {
                        setGroupCreationStatus(0)
                    } else {
                        setGroupCreationStatus(data.created_status)
                    }
                } else {
                    console.log(data)
                }
            })
            .catch(error => {
                console.log("Error!")
            })
    }

    const createGroup = async () => {
        console.log("Creating Group!")
        const requestOption = {
            method: "POST",
            credentials: "include",
            headers: { "Content-Type": "application/json"}
        }

        const response = await fetch("http://ec2-52-86-251-227.compute-1.amazonaws.com:8000/createGroupSession", requestOption)
            .then(async response => {
                const data = await response.json()
                if (response.ok) {
                    console.log(data)
                    checkGroupCreation()
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
                                    {
                                        groupCreationStatus == 0 ?
                                            <button 
                                                id="submit"
                                                className="btn dashboard-large-login move-medium w-50 mt-3"
                                                onClick={createGroup}>
                                                Create Group {'>'}
                                            </button>
                                            :
                                            <p className="move-medium black-theme mt-3">Invite your friends: http://ec2-52-86-251-227.compute-1.amazonaws.com:3000/join/group/{groupCreationStatus}</p>
                                    }
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
        </div>
    )
}

export default Group