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
            <div className="restaurant-name-row">
                <p className="font-size-md black-theme move-bold">{name}</p>
            </div>
            <div className="restaurant-image-row mt-3">
                <img className="restaurant-image w-100" src={image}></img>
            </div>
            <div className="restaurant-description-row mt-3">
                <h3 className="move-medium">{category}</h3>
                <h3 className="move-medium">{address}</h3>
            </div>
        </div>
    )
}

export default RestaurantCard