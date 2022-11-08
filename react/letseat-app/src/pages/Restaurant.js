import React, { Component } from 'react'
import { useEffect, useState } from 'react'

import TestData from '../data/test-data.json'
import RestaurantCard from '../components/RestaurantCard'

function Restaurant() {

    // Keeps index of the restaurant index from JSON data
    const [ restaurantIndex, setRestaurantIndex ] = useState(0)
    // State 0: Questionnaire, State 1: Display Restaurant
    const [ displayRestaurant, setDisplayRestaurant ] = useState(1)
    
    const nextRestaurant = () => {
        setRestaurantIndex((restaurantIndex) => restaurantIndex + 1)
    }

    const confirmRestaurant = () => {
        setDisplayRestaurant(0)
    }

    // Accesses JSON data (implement error or null checks later on)
    const parseRestaurantData = (jsonData, index) => {
        return jsonData.businesses[index]
    }

    return (
        <div className="container">
            <div className="h-100 d-flex align-items-center">
                <div className="col-md-6 mt-4 mx-auto">
                {   displayRestaurant == 0
                    ? (
                        <h1>Confirmed!</h1>
                    ) :
                    (
                        <>
                            <RestaurantCard jsonData={parseRestaurantData(TestData, restaurantIndex)} />
                            <div className="row mt-4 mb-5">
                                <div className="col-md-6 mx-auto">
                                    <button type="button" className="btn tryAgain w-100" onClick={nextRestaurant}>Try Again</button>
                                </div>
                                <div className="col-md-6 mx-auto">
                                    <button type="button" className="btn confirm w-100" onClick={confirmRestaurant}>I'm Going!</button>
                                </div>
                            </div>
                        </>
                    )
                }
                </div>
            </div>
        </div>
    );
}
  

export default Restaurant