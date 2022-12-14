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
                <p className="font-size-md colfax-medium">{name}</p>
            </div>
            <div className="restaurant-image-row mt-3">
                <img className="restaurant-image w-100" src={image}></img>
            </div>
            <div className="restaurant-description-row mt-3">
                <h3 className="colfax-regular">{category}</h3>
                <h3 className="colfax-regular">{address}</h3>
            </div>
        </div>
    )
}

export default RestaurantCard