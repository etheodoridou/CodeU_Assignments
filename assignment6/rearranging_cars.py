'''
Created on 07 July 2017

@author: Eva
'''

def print_car_moves(initial_car_park, final_car_park):
    car_moves = rearrange_cars(initial_car_park, final_car_park)
    
    for i in range(len(car_moves)):
        print(car_moves[i].__str__())

def rearrange_cars(initial_car_park, final_car_park):
    """Rearranges the cars from the initial positions to the end positions.
    
    Args:
        initial_car_park: an array, represents the initial positions of the cars in the parking lot
        final_car_park: an array, represents the final positions of the cars in the parking lot
        
    Returns:
        an array of Move objects that represent the moves taken to rearrange the cars to their final positions
    """
    if len(initial_car_park) != len(final_car_park):
        raise ValueError("must be the same length: initial_car_park, final_car_park")
    
    EMPTY_SPACE = 0
    # Dictionary used for O(1) lookups when searching for the index of a value in the car_park
    car_map = {}
    moves = []
    
    for i in range(len(initial_car_park)):
        car_map[initial_car_park[i]] = i
    
    for space in range(len(initial_car_park)):
        if initial_car_park[space] != final_car_park[space] and initial_car_park[space] != EMPTY_SPACE:
            empty_space_index = car_map[EMPTY_SPACE]
            move_car(initial_car_park, car_map, space, empty_space_index, moves)
            if initial_car_park != final_car_park:
                end_value_index = car_map[final_car_park[space]]
                move_car(initial_car_park, car_map, end_value_index, space, moves)

    return moves

def move_car(car_park, car_map, _from, _to, moves):
    # Swap the two cars in the parking lot
    swap(car_park, _from, _to)
    # Update car map to reflect parking lot
    swap(car_map, car_park[_from], car_park[_to])
    moves.append(Move(_from, _to))

def swap(array, _from, _to):
    temp = array[_from]
    array[_from] = array[_to]
    array[_to] = temp
   
class Move:
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination
    
    def get_origin(self):
        return self.origin
    
    def get_destination(self):
        return self.destination
    
    def __str__(self):
        return "Move from " + str(self.get_origin()) + " to " + str(self.get_destination())
    
        
