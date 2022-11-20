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
            <div className="d-flex align-items-center justify-content-center h-100">
                <div className="col-md-7 mt-4">
                    <div className="d-flex flex-column">
                    {   displayRestaurant == 0
                        ? (
                            <h1>Confirmed!</h1>
                        ) :
                        (
                            <>
                                <RestaurantCard jsonData={parseRestaurantData(TestData, restaurantIndex)} />
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
  

export default Restaurant