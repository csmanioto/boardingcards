# Trip Sort challenger

```
Carlos Smaniotto - January - 2018 
```

This soluction was written using Python 3

# How to run the code ?


**just execute the main.py**
 
In this case, the stack of boarding cards is a list of dict as variable "boarding_cards" into the main.py

But we can create a REST API or feeding the routine using console parameter.

# Time to create this code ? 
A warmed developer should take in less of 1 hours to create it from scratch.

# The  challenge

You are given a stack of boarding cards for various transportation types that will take you from a point A to point B via several stops on the way. All of the boarding cards are out of order and you don't know where your journey starts, nor where it ends. Each boarding card contains information about seat assignment, and means of transportation (such as flight number, bus number etc).

Write an API that lets you sort this kind of list and present back a description of how to complete your journey.

For instance the API should be able to take an unordered set of boarding cards, provided in a format defined by you, and produce this list:

1. Take train 78A from Madrid to Barcelona. Sit in seat 45B.
2. Take the airport bus from Barcelona to Gerona Airport. No seat assignment.
3. From Gerona Airport, take flight SK455 to Stockholm. Gate 45B, seat 3A. Baggage drop at ticket counter 344.
4. From Stockholm, take flight SK22 to New York JFK. Gate 22, seat 7B. Baggage will we automatically transferred from your last leg.
5. You have arrived at your final destination.



#####  Data format allowed
```
'[
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
]'
```

# The logic behind of the challenge

Don't mind the amount of bording cards you have! Do you need to know only two things:

1 - The first trip (A-B)
2 - The end trip (D-E)

With this information is easy to connect the trips because the end point of the previous trip will be the starting point of a new trip
 ```
 START: A-B
          B-C
            C-D
 END:         D-E
 ```
 
After put the trips in order, we can use the information in each boarging cards to create the correct information list.

However, case you have more one path to the same destination, we should to use the Dijkstra's Algorithm or other to find the minimum path:


In this case we need to consider the weight:
- Walking from point A to point B: 0 weight
- Take a bus from point A to point B: 1 weight
- Take a train from point A to point B: 2 weight
- Take a fight from point A to point B: 3 weight

And each point is a node of graph
