import React from 'react'
import { useParams } from 'react-router-dom'
import { useEffect, useState } from 'react'

import DashboardNavbar from '../components/DashboardComponents/DashboardNavbar';

const Group = () => {

    const { host } = useParams()
    console.log(host)

    return (
        <div className="container-fluid search-component">
            <DashboardNavbar />
            <h1 className="white-theme">Hello World! {host}</h1>
        </div>
    )
}

export default Group