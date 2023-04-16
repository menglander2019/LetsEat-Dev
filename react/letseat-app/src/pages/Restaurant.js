import React, { Component } from 'react'
import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom';

import TestData from '../data/test-data.json'
import RestaurantCard from '../components/RestaurantCard'
import DashboardNavbar from '../components/DashboardComponents/DashboardNavbar';
import LoadingAnimation from '../components/LoadingAnimation';

import '../css/Restaurant.css';

import url from '../WebsiteURL'

function Restaurant() {

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

        await fetch(url + "getRecommendations/", requestOption)
            .then(async response => {
                const data = await response.json()
                if (response.ok) {
                    console.log(data.restaurants)
                    setRestaurantList(data.restaurants)
                    if (data.restaurants.length == 0) {
                        navigate("/restaurant/results/none")
                    }
                } else {
                    console.log("Error!")
                }
            })
            .catch(error => {
                console.log("Error!")
            })
    }

    const nextRestaurant = async (e) => {
        if (restaurantIndex + 1 >= restaurantList.length) {
            navigate("/restaurant/results/none")
        }
        setRestaurantIndex((restaurantIndex) => restaurantIndex + 1)
        const requestOption = {
            method: "POST",
            credentials: "include",
            headers: { "Content-Type": "application/json"},
            body: JSON.stringify(restaurantList[restaurantIndex])
        }

        await fetch(url + "restaurantDenied/", requestOption)
            .then(async response => {
                const data = await response.json()
                if (response.ok) {
                    console.log("Successful sent denial of:")
                    console.log(restaurantList[restaurantIndex])
                } else {
                    console.log("Error!")
                }
            })
            .catch(error => {
                console.log("Error!")
            })
    }

    const confirmRestaurant = async (e) => {
        setDisplayRestaurant(0)
        const requestOption = {
            method: "POST",
            credentials: "include",
            headers: { "Content-Type": "application/json"},
            body: JSON.stringify(restaurantList[restaurantIndex])
        }

        await fetch(url + "restaurantAccepted/", requestOption)
            .then(async response => {
                const data = await response.json()
                if (response.ok) {
                    console.log("Successful sent acceptance of:")
                    console.log(restaurantList[restaurantIndex])
                } else {
                    console.log("Error!")
                }
            })
            .catch(error => {
                console.log("Error!")
            })
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
                    <div className="col-md-6 mt-5">
                        <div className="restaurant-main-block">
                            <div className="d-flex flex-column">
                                {   displayRestaurant == 0
                                    ? (
                                        <>
                                            <h1 className="move-medium black-theme text-center">Confirmed!</h1>
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
  

export default Restaurant