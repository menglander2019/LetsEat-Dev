import React, { Component } from 'react'
import { useEffect, useState } from 'react'

import TestData from '../data/test-data.json'
import RestaurantCard from '../components/RestaurantCard'
import DashboardNavbar from '../components/DashboardComponents/DashboardNavbar';

function Restaurant() {

    const [ restaurantList, setRestaurantList ] = useState([])
    // Keeps index of the restaurant index from JSON data
    const [ restaurantIndex, setRestaurantIndex ] = useState(0)
    // State 0: Questionnaire, State 1: Display Restaurant
    const [ displayRestaurant, setDisplayRestaurant ] = useState(1)
    
    useEffect(() => {
        fetchRestaurants()
    }, [])

    // Calls FastAPI to pull questions
    const fetchRestaurants = async (e) => {
        console.log("Restaurants Fetched!")
        const requestOption = {
            method: "GET",
            credentials: "include",
            headers: { "Content-Type": "application/json"}
        }

        await fetch("http://localhost:8000/getRecommendations/", requestOption)
            .then(async response => {
                const data = await response.json()
                if (response.ok) {
                    console.log(data.restaurants)
                    setRestaurantList(data.restaurants)
                } else {
                    console.log("Error!")
                }
            })
            .catch(error => {
                console.log("Error!")
            })
    }

    const nextRestaurant = () => {
        setRestaurantIndex((restaurantIndex) => restaurantIndex + 1)
    }

    const confirmRestaurant = () => {
        setDisplayRestaurant(0)
    }

    // Accesses JSON data (implement error or null checks later on)
    const parseRestaurantData = (index) => {
        return restaurantList[index]
    }

    if (restaurantList.length == 0) {
        return ( <h1>Loading</h1>)
    } else {
        return (
            <div className="container">
                <DashboardNavbar navBarColor={"home-navbar-white"}/>
                <div className="d-flex align-items-center justify-content-center h-100">
                    <div className="col-md-6 mt-3">
                        <div className="d-flex flex-column">
                        {   displayRestaurant == 0
                            ? (
                                <>
                                    <h1 className="text-center">Confirmed!</h1>
                                </>
                            ) :
                            (
                                <>
                                    <RestaurantCard jsonData={parseRestaurantData(restaurantIndex)} />
                                    <div className="buttons mt-4">
                                        <div className="d-flex flex-wrap justify-content-between">
                                            <button type="button" className="btn tryAgain flex-styling-50" onClick={nextRestaurant}>Try Again</button>
                                            <button type="button" className="btn confirm flex-styling-50" onClick={confirmRestaurant}>I'm Going!</button>
                                        </div>
                                    </div>
                                </>
                            )
                        }
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}
  

export default Restaurant