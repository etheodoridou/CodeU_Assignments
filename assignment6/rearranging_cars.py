'''
Created on 07 July 2017

@author: Eva
'''

def print_car_moves(initial_car_park, final_car_park):
    """
    Prints the moves required to rearrange the cars from the initial positions to the end positions.
    
    Args:
        initial_car_park:   an array, represents the initial positions 
                            of the cars in the parking lot
        final_car_park:     an array, represents the final positions of
                            the cars in the parking lot
    """
    rearranging_moves = rearrange_cars(initial_car_park, final_car_park)
    
    for i in rearranging_moves:
        print(i)
    print("{} moves in total.".format(len(rearranging_moves)))

def rearrange_cars(initial_car_park, final_car_park):
    """
    Rearranges the cars from the initial positions to the end positions.
    
    Args:
        initial_car_park:   an array, represents the initial positions
                            of the cars in the parking lot
        final_car_park:     an array, represents the final positions 
                            of the cars in the parking lot
        
    Returns:
        an array of Move objects that represent the moves taken to rearrange the cars to their final positions
    """
    if len(initial_car_park) != len(final_car_park):
        raise ValueError("must be the same length: initial_car_park, final_car_park")
    
    EMPTY_SPACE = 0
    CAR_PARK_SIZE = len(initial_car_park)
    # List used for O(1) lookups when searching for the index of a value in the car_park
    car_positions = [0] * CAR_PARK_SIZE
    moves = []
    
    for i in range(CAR_PARK_SIZE):
        car_at_i = initial_car_park[i]
        car_positions[car_at_i] = i
    
    for space in range(CAR_PARK_SIZE):
        if initial_car_park[space] != final_car_park[space]:
            if initial_car_park[space] != EMPTY_SPACE:
                empty_space_index = car_positions[EMPTY_SPACE]
                new_move = move_car(initial_car_park, car_positions, space, empty_space_index)
                moves.append(new_move)
        if initial_car_park[space] != final_car_park[space]:
            end_value_index = car_positions[final_car_park[space]]
            new_move = move_car(initial_car_park, car_positions, end_value_index, space)
            moves.append(new_move)
     
    return moves

def move_car(car_park, car_map, _from, _to):
    """
    Swaps the positions of two cars in the parking lot and updates the map of car positions accordingly.
    
    Args:
        car_park:   an array, represents the positions of the cars in the parking lot
        car_map:    a list, records the index of each car in the car park to improve performance
        _from:      an integer, represents the source index of the car in the car park
        _to:        an integer, represents the index in the car park to which the car will be moved
        
    Returns:
        a Move object that represents the move taken to switch the positions of the two cars.
    """
    src_pos = car_park[_from]
    dest_pos = car_park[_to]
    car_park[_from], car_park[_to] = car_park[_to], car_park[_from]
    car_map[src_pos], car_map[dest_pos] = car_map[dest_pos], car_map[src_pos]
    
    return Move(_from, _to)
   
class Move:
    """
    Move objects store information about movement of a car in the parking lot.
    Each move object has two fields that record the origin and destination of the movement.
    """
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination
    
    def get_origin(self):
        return self.origin
    
    def get_destination(self):
        return self.destination
    
    def __eq__(self, other):
        return (self.origin == other.origin and
                self.destination == other.destination)
        
    def __str__(self):
        return "Move car from {} to {}".format(self.get_origin(), self.get_destination())
    
        
