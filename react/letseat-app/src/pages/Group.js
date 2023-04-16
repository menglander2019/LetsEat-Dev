import React from 'react'
import { useParams } from 'react-router-dom'
import { useEffect, useState } from 'react'

import DashboardNavbar from '../components/DashboardComponents/DashboardNavbar';

import '../css/Group.css';

import url from '../WebsiteURL'
import web_url from '../WebsiteURLFront'

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

        const response = await fetch(url + "createdGroupStatus", requestOption)
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

        const response = await fetch(url + "createGroupSession", requestOption)
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

    const deleteGroup = (e) => {

        const requestOption = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            credentials: "include",
        }

        const response = fetch(url + "deleteGroupSession", requestOption)   
            .then(response => {
                if (response.ok) {
                    console.log("Deleted Group!")
                    checkGroupCreation()
                } else {
                    console.log("Error Deleting Group!")
                }
            })
            .catch(error => {
                console.log("Error deleteGroup!")
            })
    }

    return (
        <div className="container-fluid dashboard-component">
            <div className="d-flex flex-column">
                <DashboardNavbar />
                <div className="dashboard-banner">
                    <div className="d-flex">
                        <div className="col-md-6">
                            <div className="d-flex justify-content-center">
                                <div className="col-md-8 padding-style-7">
                                    <div className="d-flex flex-column">
                                    <h3 className="move-medium black-theme">Group Settings</h3>
                                    <p className="move-medium grey-theme">Create a group and invite your friends to join your search with their own preferences</p>
                                    {
                                        groupCreationStatus == 0 ?
                                            <button 
                                                id="submit"
                                                className="btn dashboard-large-login move-medium w-100 mt-2"
                                                onClick={createGroup}>
                                                Create Group
                                            </button>
                                            :
                                            <p className="move-medium black-theme mt-3">Invite your friends: {web_url}join/group/{groupCreationStatus}</p>
                                    }
                                    {
                                        groupCreationStatus != 0 ?
                                            <button 
                                                id="submit"
                                                className="btn dashboard-large-login-red move-medium w-100 mt-2"
                                                onClick={deleteGroup}>
                                                Delete Group
                                            </button>
                                            :
                                            <button 
                                                id="submit"
                                                className="btn dashboard-large-login move-medium disabled w-100 mt-2"
                                                onClick={deleteGroup}>
                                                Delete Group
                                            </button>

                                }
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
            
    )
}

export default Group