# "Aroma" API

Our API, built with Django and Python, is an API with one model - a database of wines containing ids of their specific information.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
You need python community and django installed on your machine.

```

### Installing

1. Fork and clone this repository.
1. Change into the new directory and create a development branch to work on.



#### Endpoint to fetch the data of all movies in the database

https://aroma-backend.herokuapp.com/wines/

## API

API

```json
    {
        "id": 1,
        "sku": "a547352f-13f1-4d0c-b6df-31bb9153a66c",
        "brand_name": "Quintessa",
        "type_name": "Bordeaux Blend",
        "wine_type": "Red",
        "location": "Rutherford, USA",
        "image_url": "https://www.wine-searcher.com/images/labels/00/61/10560061.jpg?width=133&height=196&fit=bounds&canvas=133,196",
        "description": "A Bordeaux Blend, at its most basic, is any combination of those grape varieties typically used to make the red wines of Bordeaux. The phrase, which seems to have originated with British wine merchants in the 19th Century, relates as much to wines made from the blend as to the grape variety combination itself (© Copyright material, Wine-Searcher.com). Far from being an officially defined or legal term, it is almost never used for wine-labeling purposes (although it occasionally appears on back labels). Its equivalent in the United States is Meritage, which is not only legally defined, but also a registered trademark.  Red Bordeaux Blends are known for their powerful structure and deep flavors. Dark fruits and berries such as plum and blackcurrant are commonly used to describe the flavors of red Bordeaux, although there is an unlimited range of terms that have been ascribed to them. Tannins tend to be relatively high in these wines, giving them a firm structure.",
        "price": "196.00",
        "wine_year": "2017"
    }
```

## Deployment

Add additional notes about how to deploy this on a live system

## Contributing

If you want to contribute to this project, you can [submit an issue](https://github.com/aroma-backend/issues) on this repository.

## Versioning

We use [Github](http://github.com) for versioning.

## Authors

- **Roshonia Brooks** - [RoshoniaB](https://github.com/RoshoniaB)


## Acknowledgments

- [Wine Searcher](https://www.wine-searcher.com/)