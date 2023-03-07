import React, { Component } from 'react'
import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom';

import TestData from '../data/test-data.json'
import RestaurantCard from '../components/RestaurantCard'
import DashboardNavbar from '../components/DashboardComponents/DashboardNavbar';
import LoadingAnimation from '../components/LoadingAnimation';

import '../css/Restaurant.css';

function GroupRestaurant() {

    const navigate = useNavigate()
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

        await fetch("http://ec2-54-160-112-17.compute-1.amazonaws.com:8000/getGroupRestaurants/", requestOption)
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

    const backButton = () => {
        navigate("/dashboard")
    }

    if (restaurantList.length == 0) {
        return ( <LoadingAnimation />)
    } else {
        return (
            <div className="container-fluid restaurant-component">
                <DashboardNavbar />
                <div className="d-flex justify-content-center h-100">
                    <div className="col-md-6">
                        <div className="restaurant-main-block">
                            <div className="d-flex flex-column">
                                {   displayRestaurant == 0
                                    ? (
                                        <>
                                            <h1 className="text-center">Confirmed!</h1>
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
                                        </>
                                    ) :
                                    (
                                        <>
                                            <RestaurantCard jsonData={parseRestaurantData(restaurantIndex)} />
                                            <div className="buttons mt-3">
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
            </div>
        );
    }
}
  

export default GroupRestaurant