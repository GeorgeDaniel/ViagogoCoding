import random
from random import randint

'''
This method is the backbone of the program. It creates random event coordinates and it makes sure that they are not 
repetead since we can only have one event per pair of coordinates. It also find out the distance between the event's
location and the location of the user, using the Manhattan distance.
'''
def generate_events_distances(m, coord_list, distance_list, a, b):
    '''
    We create the first even separately. We did this so we can compare the next with an already
    existing event and by doing so making sure we dont repeat any coordinates
    '''

    #These two variables are X and Y corresponding to the location of the user introduced
    original_x = a
    original_y = b

    '''
    Here we create our first event, using random coordinates and calculating its distance from the user's location
    '''
    x = randint(-10, 10)
    y = randint(-10, 10)

    distance = abs(a - x) + abs(b - y)
    distance_list.append(distance)
    '''
    We store the coordinates of the new event in a touple that we add to our dictionary that will offer us an
    overview over the whole board's details allowing us to figure out if the user gets the correct information
    '''
    rand_tuple = (x, y)
    coord_list.append(rand_tuple)

    '''
    In this method 'i' helps us make multiple tries of random generated coordinates until the result is unique for 
    our list of events, if we found a unique set of coordinates we increment 'i' allowing us to get closer to the 
    number of events we want, if not we will repeat the process until we manage to do so.
    '''
    i = 1
    #Repeating the whole process we did above for the number of the events we desire
    while i < m:
        x = randint(-10, 10)
        y = randint(-10, 10)
        rand_tuple = (x, y)

        '''
        For each tuple of coordinates we check if it any previous tuple(which contain the coordinates of other events)
        if so we increment the number of matches
        '''
        match_tuple = 0
        for current in range(len(coord_list)):
            #Variable that represents one of our already existing touples
            current_touples = coord_list[current]
            if all(rand_tuple == current_touples for rand_tuple, current_touples in zip(rand_tuple, current_touples)) == True:
                match_tuple += 1

        '''
        If the touple we created passes the matching test we continue and add it to our dictionary, calculate its distrance
        from the user's location and add that to the dictionary aswell, and increment i since we found a desired result
        '''
        if match_tuple == 0:
            coord_list.append(rand_tuple)
            distance = abs(original_x - x) + abs(original_y - y)
            distance_list.append(distance)
            i += 1

'''
Simple method that finds the chepeast ticket in a list of prices which I will use in the more complex methods
'''
def find_cheapest_ticket(list):
    min = list[1]
    for i in list:
        if i < min:
            min = i
    return min

'''
This method generates the random list of prices for each event, for simplicty I chose to also find the chepeast ticket
and add it in the dictionary, since we are only interested in the cheapest ticket. By already finding the
cheapest ticket in this method I save time and the code is more concise.
'''
def make_prices_list(m, dictionary, touples, distance_list, nr_tickets):

    '''
    The whole process is repetead multiple times depending on the number of events we have, after we randomly generate
    a number of prices we use another method I created to find the cheapest ticket and add it to the dictionary.
    '''
    i = 0;
    while i < m:
        my_list = []
        j = 0
        while j < nr_tickets:
            x = round(random.uniform(0, 50), 6)
            g = float("{0:.2f}".format(x))
            my_list.append(g)
            j += 1

        '''
        After I find the cheapest ticket I add it in a touple together with the distance for that even and pass it 
        to the dictionary(at the coressponding key in the dictionary)
        '''
        my_min = find_cheapest_ticket(my_list)
        dictionary[touples[i]] = (my_min, distance_list[i])
        i += 1



'''
Method that find our closest 5 events, to find them in one go I used two lists. One is used to store the index of 
the closest events in the order of their closenes to the user's location. The other lists(which I make a backup for)
is made out of the distances from the user of the events, in the order they were created in the begining.
My solution here was to find the smallest distrance then replace it with -1 so I can still work with the list and not
have to remove elements. I could have used linked lists, but for this small scale of only 5 events it works fast this
 way too
'''
def find_closest_five(list, otherlist):
    j = 0;
    while j < 5:
        min = 99
        for i in list:
            if i <= min and i != -1:
                min = i
                my_index = list.index(i)
        otherlist.append(my_index)
        list[my_index] = -1
        j += 1

'''Last method I created used to print the desire result, it is a simple method that makes use of the lists
we created so far.'''
def print_events(dictionary, mylist):
    i = 0
    example = list(dictionary.values())
    while i < 5:

        print("Event", mylist[i], "- $", example[mylist[i]][0], ", Distance ", reserve_distances[mylist[i]])
        i +=1

'''
After I finished creating my helped methods I then create any dictionary, variable, list that I will need to feed
into the methods to achieve the desired result
'''
#Providing a random seed based on the current time
random.seed()

#The dictionary and list that will be manipulated in order to achieve the desired result, with self explanatory names
dict_event = {}
my_coordinates = []
my_distances = []
my_five_smallest = []
'''
N gets a random val from 6 since its the nminimum number of events needed to prove that my program works
The maximum number of events depends on the preferences, it can have the whole board to test it, or it can have any
other random number, but not bigger then the board
'''
n = randint(6, 100)

#We get the coordinates for the event from the user and store them in variables
my_inputs = input("Enter coordinates: ")
(my_a, sep, my_b) = my_inputs.strip().partition(',')
int_a = int(my_a)
int_b = int(my_b)

#We start generating the needed information using the helped methods
generate_events_distances(n, my_coordinates, my_distances, int_a, int_b)

'''
Since my method of finding the 5 closest events was a bit weird, I needed a reserve list to get the original indexes
of the events, this list only contains the distances in their original order, its a clone of "my_distances"
'''
reserve_distances = list(my_distances)

'''We start creating the prices and also finding the cheapest ticket, the 5 at the end represents the number of tickets
per event, which I considered to simulate reality since there won't be too many types of tickets for an event
It can be increased or decreased without affecting the program'''
make_prices_list(n, dict_event, my_coordinates, my_distances, 5)

find_closest_five(my_distances, my_five_smallest)

#Apart from the desired output I also print the dictionary holding the information I used so I can check if everything
#is right, this only works for small numbers since we can't get a dictionary with hundreds of entries
print("The following world was generated randomly:")
print(dict_event)
print_events(dict_event, my_five_smallest)









