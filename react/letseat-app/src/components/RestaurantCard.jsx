import React, { Component } from 'react'

// Takes in JSON data of a restaurant and parses the data
const RestaurantCard = ({ jsonData }) => {

    let exampleRestaurant = jsonData
    let name = exampleRestaurant.name
    let image = exampleRestaurant.image_url
    let address = exampleRestaurant.location.address1
    let category = exampleRestaurant.categories[0].title
    let price = exampleRestaurant.price
    let display_phone = exampleRestaurant.display_phone
 
    return (
        <div className="restaurant">
            <div className="restaurant-name-row">
                <h1 className="black-theme move-medim">{name}</h1>
            </div>
            <div className="restaurant-image-row mt-3">
                <img className="restaurant-image w-100" src={image}></img>
            </div>
            <div className="restaurant-description-row mt-3">
                <div className="d-flex flex-wrap">
                    <div className="d-flex col-md-6">
                        <h4 className="black-theme move-medium">{category}</h4>
                    </div>
                    <div className="d-flex col-md-6">
                        <h4 className="black-theme move-medium">{price}</h4>
                    </div>
                    <div className="d-flex col-md-6">
                        <h4 className="black-theme move-medium">{address}</h4>
                    </div>
                    <div className="d-flex col-md-6">
                        <h4 className="black-theme move-medium">{display_phone} </h4>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default RestaurantCard