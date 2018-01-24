class Trip(object):
    """
     Case use Dijkstra's Algorithm, we need to create a weight from each trip.
    """
    weight_list = [
        {'name': 'walk', 'weight': 0},
        {'name': 'bus', 'weight': 1},
        {'name': 'train', 'weight': 2},
        {'name': 'flight', 'weight': 3},

    ]

    boarding_cards = None

    def __init__(self, boarding_cards=None):
        self.boarding_cards = boarding_cards
        pass

    # I decided to use a simple way to discovery the fist trip.
    # The initial trip should not be as a destination in the other cards
    def getStartPoint(self):
        trip_started_from = None
        from_lits_filtred = []
        all_from_list = []
        for x in self.boarding_cards:
            all_from_list.append(x['from'])
            for y in self.boarding_cards:
                if x['from'] == y['to']:
                    from_lits_filtred.append(x['from'])  # Found all trips with connections
        # The source path is in the excluded list...
        trip_started_from = [item for item in all_from_list if item not in from_lits_filtred][0]
        trip_started = next((trip for trip in self.boarding_cards if trip['from'] == trip_started_from), None)
        return trip_started

    # I decided to use a simple way to discovery the final trip.
    # The final trip should not be as a source in the other cards
    def getEndPoint(self):
        trip_started_from = None
        from_lits_filtred = []
        all_from_list = []
        for x in self.boarding_cards:
            all_from_list.append(x['from'])
            for y in self.boarding_cards:
                if x['to'] == y['from']:
                    from_lits_filtred.append(x['from'])
        trip_started_from = [item for item in all_from_list if item not in from_lits_filtred][0]
        trip_started = next((trip for trip in self.boarding_cards if trip['from'] == trip_started_from), None)
        return trip_started

    # Sort the boarding cards in List format
    def getPathList(self):
        start_node = self.getStartPoint()
        end_node = self.getEndPoint()

        sorted_list = [start_node]
        while True:
            for card in self.boarding_cards:
                if card['from'] == start_node['to']:
                    sorted_list.append(card)
                    start_node = card
            if end_node in sorted_list:
                break

        return sorted_list

    # Show the boarding cards list in instructions format
    def getPath(self):

        instructions = None
        instruction_list = []
        path_list = self.getPathList()
        idx = 1
        for path in path_list:

            if path['transportation'] == "bus":
                instructions = "{}. Take the {} from {} to Gerona {}. No seat assignment.".format(idx,
                                                                                                  path['transportation'],
                                                                                                  path['from'],
                                                                                                  path['to'])
                instruction_list.append(instructions)
                idx += 1

            if path['transportation'] == "train":
                instructions = "{}. Take {} {} from {} to {}. Sit in seat {}".format(idx,
                                                                                     path['transportation'],
                                                                                     path['transportation_number'],
                                                                                     path['from'],
                                                                                     path['to'],
                                                                                     path['seat'])
                instruction_list.append(instructions)
                idx += 1

            if path['transportation'] == "flight":
                instructions = "{}. From {}, take {} {} to {}. Gate {} ,sit in seat {}.".format(idx,
                                                                                                path['from'],
                                                                                                path['transportation'],
                                                                                                path['transportation_number'],
                                                                                                path['to'],
                                                                                                path['Gate'],
                                                                                                path['seat'])
                instruction_list.append(instructions)
                idx += 1
                try:
                    if path['baggage']:
                        instructions = "{}. Baggage drop at ticket counter {}.".format(idx, path['baggage'])
                        instruction_list.append(instructions)
                        idx += 1
                except Exception as error:
                    pass

        for instruction in instruction_list:
            print(instruction)
