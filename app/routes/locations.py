from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/locations", tags=["locations"])

locations = [
    {
        "id": 0,
        "name": "Acme Fresh Start Housing",
        "city": "Chicago",
        "state": "IL",
        "photo": "https://angular.dev/assets/images/tutorials/common/bernard-hermant-CLKGGwIBTaY-unsplash.jpg",
        "availableUnits": 4,
        "wifi": True,
        "laundry": True,
    },
    {
        "id": 1,
        "name": "A113 Transitional Housing",
        "city": "Santa Monica",
        "state": "CA",
        "photo": "https://angular.dev/assets/images/tutorials/common/brandon-griggs-wR11KBaB86U-unsplash.jpg",
        "availableUnits": 0,
        "wifi": False,
        "laundry": True,
    },
    {
        "id": 2,
        "name": "Warm Beds Housing Support",
        "city": "Juneau",
        "state": "AK",
        "photo": "https://angular.dev/assets/images/tutorials/common/i-do-nothing-but-love-lAyXdl1-Wmc-unsplash.jpg",
        "availableUnits": 1,
        "wifi": False,
        "laundry": False,
    },
    {
        "id": 3,
        "name": "Homesteady Housing",
        "city": "Chicago",
        "state": "IL",
        "photo": "https://angular.dev/assets/images/tutorials/common/ian-macdonald-W8z6aiwfi1E-unsplash.jpg",
        "availableUnits": 1,
        "wifi": True,
        "laundry": False,
    },
    {
        "id": 4,
        "name": "Happy Homes Group",
        "city": "Gary",
        "state": "IN",
        "photo": "https://angular.dev/assets/images/tutorials/common/krzysztof-hepner-978RAXoXnH4-unsplash.jpg",
        "availableUnits": 1,
        "wifi": True,
        "laundry": False,
    },
    {
        "id": 5,
        "name": "Hopeful Apartment Group",
        "city": "Oakland",
        "state": "CA",
        "photo": "https://angular.dev/assets/images/tutorials/common/r-architecture-JvQ0Q5IkeMM-unsplash.jpg",
        "availableUnits": 2,
        "wifi": True,
        "laundry": True,
    },
    {
        "id": 6,
        "name": "Seriously Safe Towns",
        "city": "Oakland",
        "state": "CA",
        "photo": "https://angular.dev/assets/images/tutorials/common/phil-hearing-IYfp2Ixe9nM-unsplash.jpg",
        "availableUnits": 5,
        "wifi": True,
        "laundry": True,
    },
    {
        "id": 7,
        "name": "Hopeful Housing Solutions",
        "city": "Oakland",
        "state": "CA",
        "photo": "https://angular.dev/assets/images/tutorials/common/r-architecture-GGupkreKwxA-unsplash.jpg",
        "availableUnits": 2,
        "wifi": True,
        "laundry": True,
    },
    {
        "id": 8,
        "name": "Seriously Safe Towns",
        "city": "Oakland",
        "state": "CA",
        "photo": "https://angular.dev/assets/images/tutorials/common/saru-robert-9rP3mxf8qWI-unsplash.jpg",
        "availableUnits": 10,
        "wifi": False,
        "laundry": False,
    },
    {
        "id": 9,
        "name": "Capital Safe Towns",
        "city": "Portland",
        "state": "OR",
        "photo": "https://angular.dev/assets/images/tutorials/common/webaliser-_TPTXZd9mOo-unsplash.jpg",
        "availableUnits": 6,
        "wifi": True,
        "laundry": True,
    },
    {
        "id": 10,
        "name": "New Test Location 1",
        "city": "Portland",
        "state": "OR",
        "photo": "https://angular.dev/assets/images/tutorials/common/r-architecture-GGupkreKwxA-unsplash.jpg",
        "availableUnits": 6,
        "wifi": True,
        "laundry": True,
    }
]

@router.get("")
def get_locations():
    return locations

@router.get("/{id}")
def get_location(id: int):
    for location in locations:
        if location["id"] == id:
            return location

    raise HTTPException(status_code=404, detail="Location not found")
