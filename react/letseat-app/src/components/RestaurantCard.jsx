import React, { Component } from 'react'

// Takes in JSON data of a restaurant and parses the data
const RestaurantCard = ({ jsonData }) => {

    let exampleRestaurant = jsonData
    let name = exampleRestaurant.name
    let image = exampleRestaurant.image_url
    let address = exampleRestaurant.location.address1
    let category = exampleRestaurant.categories[0].title
 
    return (
        <div className="restaurant">
            <div className="restaurant-name-row mt-3">
                <h1 className="display-4">{name}</h1>
            </div>
            <div className="restaurant-image-row mt-3">
                <img className="restaurant-image w-100" src={image}></img>
            </div>
            <div className="restaurant-description-row mt-3">
                <h2>{category}</h2>
                <h2>{address}</h2>
            </div>
        </div>
    )
}

export default RestaurantCard