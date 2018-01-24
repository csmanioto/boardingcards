from sortcards import Trip

boarding_cards=[
    {
        "from":"Gerona Airport",
        "to":"Stockholm",
        "transportation":"flight",
        "transportation_number":"SK455",
        "seat":"3A",
        "Gate":"45B",
        "baggage":"344"
    },
    {
        "from":"Madrid",
        "to":"Barcelona",
        "transportation":"train",
        "transportation_number":"78A",
        "seat":"45B"
    },
    {
        "from":"Stockholm",
        "to":"New York JFK",
        "transportation":"flight",
        "transportation_number":"SK22",
        "seat":"7B",
        "Gate":"22"
    },
    {
        "from":"Barcelona",
        "to":"Gerona Airport",
        "transportation":"bus"
    }
]


if __name__ == '__main__':
    trip = Trip(boarding_cards)
    # I just comment to show how works this code...
    #print(trip.getPathList())
    #print(trip.getStartPoint())
    #print(trip.getEndPoint())

    # Finally the instructions.
    trip.getPath()
