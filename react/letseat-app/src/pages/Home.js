import React, { Component } from 'react'
import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import 'bootstrap/dist/css/bootstrap.css'
import '../css/Home.css';

import HomeDescription from '../components/HomeComponents/HomeDescription';
import HomeBanner from '../components/HomeComponents/HomeBanner';
import HomeNavbar from '../components/HomeComponents/HomeNavbar';

function Home() {
    return (
        <div className="container-fluid">
            <div className="d-flex flex-column">
                <HomeNavbar />
                <HomeBanner />
                <HomeDescription />
                <div className="row mt-5">
                    <Link to="/login">
                        <span>Login</span>
                    </Link><br />
                    <Link to="/createaccount">
                        <span>Create Account</span>
                    </Link><br />
                    <Link to="/edit/account">
                        <span>Edit Account</span>
                    </Link><br />
                    <Link to="/edit/preferences">
                        <span>Profile Questions</span>
                    </Link><br />
                    <Link to="/searchquestions">
                        <span>Search Questions</span>
                    </Link><br />
                    <Link to="/restaurantsearch">
                        <span>Restaurant</span>
                    </Link>
                </div>
            </div>
        </div>
    );
}
  

export default Home