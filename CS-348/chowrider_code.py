from expand import expand
from collections import deque
import queue
# TO DO: Implement Breadth-first Search.
def breadth_first_search(time_map, start, end):
    """
    Breadth-first Search

    Args:
        time_map (dict): A map containing travel times between connected nodes (places or intersections), where every
        node is a dictionary key, and every value is an inner dictionary whose keys are the children of that node and
        values are travel times. Travel times are "null" for nodes that are not connected.
        start (str): The name of the node from where to start traversal
        end (str): The name of the node where to end traversal

    Returns:
        visited (list): A list of visited nodes in the order in which they were visited
        path (list): The final path found by the search algorithm
    """
    prev = {start: None}
    visited = []
    q = deque()
    q.append(start)

    while q:
        curr = q.popleft()
        visited.append(curr)
        if curr == end:
            i = end
            lst = []
            while i is not None:
                lst.append(i)
                i = prev[i]
            return visited, lst[::-1]
        for next in list(expand(curr, time_map)):
            if next not in prev:
                prev[next] = curr
                q.append(next)
    return None
    
# TO DO: Implement Depth-first Search.
def depth_first_search(time_map, start, end):
    """
    Depth-first Search

    Args:
        time_map (dict): A map containing travel times between connected nodes (places or intersections), where every
        node is a dictionary key, and every value is an inner dictionary whose keys are the children of that node and
        values are travel times. Travel times are "null" for nodes that are not connected.
        start (str): The name of the node from where to start traversal
        end (str): The name of the node where to end start traversal

    Returns:
        visited (list): A list of visited nodes in the order in which they were visited
        path (list): The final path found by the search algorithm
    """
    prev = {start: None}
    visited = []
    q = deque()
    q.append(start)

    while q:
        curr = q.pop()
        if curr in visited:
            continue
        visited.append(curr)
        if curr == end:
            i = end
            lst = []
            while i is not None:
                lst.append(i)
                i = prev[i]
            return visited, lst[::-1]
        for next in list(expand(curr, time_map)):
            if next not in visited:
                prev[next] = curr
                q.append(next)
    return None
    

# TO DO: Implement Greedy Best-first Search.
def best_first_search(dis_map, time_map, start, end):
    """
    Greedy Best-first Search

    Args:
        time_map (dict): A map containing travel times between connected nodes (places or intersections), where every
        node is a dictionary key, and every value is an inner dictionary whose keys are the children of that node and
        values are travel times. Travel times are "null" for nodes that are not connected.
        dis_map (dict): A map containing straight-line (Euclidean) distances between every pair of nodes (places or
        intersections, connected or not), where every node is a dictionary key, and every value is an inner dictionary whose keys are the
        children of that node and values are straight-line distances.
        start (str): The name of the node from where to start traversal
        end (str): The name of the node where to end traversal

    Returns:
        visited (list): A list of visited nodes in the order in which they were visited
        path (list): The final path found by the search algorithm
    """
    q = queue.PriorityQueue()
    prev = {start: None}
    q.put((0, 0,start))
    visited = []
    counter = 0

    while q:
        curr = q.get()[2]
        if curr in visited: 
            continue
        visited.append(curr)
        if curr == end:
            i = end
            lst = []
            while i is not None:
                lst.append(i)
                i = prev[i]
            return visited, lst[::-1]
        for next in list(expand(curr, time_map)):
            counter += 1
            if next not in visited:
                prev[next] = curr
                q.put((dis_map[next][end], -counter, next))
    return None


    ##set up priority Qqueue
    ## set up previous dict: {place, previous}
    ## add (0,start)
    ## start loop and pull top
    ## get children and measure distance from node to child with time map
    ## add all children and their times (addition of time to get to "node" and the time map time)
    ## repeat till you find OG node

    ## set up path compression loop
    ## start with and append each succesor
    pass

# TO DO: Implement A* Search.
def a_star_search(dis_map, time_map, start, end):
    """
    A* Search

    Args:
        time_map (dict): A map containing travel times between connected nodes (places or intersections), where every
        node is a dictionary key, and every value is an inner dictionary whose keys are the children of that node and
        values are travel times. Travel times are "null" for nodes that are not connected.
        dis_map (dict): A map containing straight-line (Euclidean) distances between every pair of nodes (places or
        intersections, connected or not), where every node is a dictionary key, and every value is an inner dictionary whose keys are the
        children of that node and values are straight-line distances.
        start (str): The name of the node from where to start traversal
        end (str): The name of the node where to end traversal

    Returns:
        visited (list): A list of visited nodes in the order in which they were visited
        path (list): The final path found by the search algorithm
    """

    q = queue.PriorityQueue()
    prev = {start: None}
    from_x_to_a = {start: 0}
    q.put((0, 0,start))
    visited = []

    while q:
        curr = q.get()[2]
        visited.append(curr)
        if curr == end:
            i = end
            lst = []
            while i is not None:
                lst.append(i)
                i = prev[i]
            return visited, lst[::-1]
        for next in list(expand(curr, time_map)):
            ##measure how long it is to get there and update fromxtoa if need be
            if next in from_x_to_a:
                if from_x_to_a[next] > from_x_to_a[curr] + time_map[curr][next]:
                    from_x_to_a[next] = from_x_to_a[curr] + time_map[curr][next]
                    prev[next] = curr
            else:
                from_x_to_a[next] = from_x_to_a[curr] + time_map[curr][next]
                prev[next] = curr
            ##add all of the children to the queue with their total distance from start and distance to end heuristic
            q.put((from_x_to_a[next] + dis_map[next][end], -from_x_to_a[next], next))
    return None
