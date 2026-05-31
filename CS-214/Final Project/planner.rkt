#lang dssl2

let eight_principles = ["Know your rights.",
"Acknowledge your sources.",
"Protect your work.",
"Avoid suspicion.",
"Do your own work.",
"Never falsify a record or permit another person to do so.",
"Never fabricate data, citations, or experimental results.",
"Always tell the truth when discussing your work with your instructor."]

# Final project: Trip Planner

import cons
import sbox_hash
import 'project-lib/stack-queue.rkt'
import 'project-lib/dictionaries.rkt'
import 'project-lib/graph.rkt'
import 'project-lib/binheap.rkt'
### Basic Types ###

#  - Latitudes and longitudes are numbers:
let Lat?  = num?
let Lon?  = num?

#  - Point-of-interest categories and names are strings:
let Cat?  = str?
let Name? = str?

### Raw Item Types ###

#  - Raw positions are 2-element vectors with a latitude and a longitude
let RawPos? = VecKC[Lat?, Lon?]

#  - Raw road segments are 4-element vectors with the latitude and
#    longitude of their first endpoint, then the latitude and longitude
#    of their second endpoint
let RawSeg? = VecKC[Lat?, Lon?, Lat?, Lon?]

#  - Raw points-of-interest are 4-element vectors with a latitude, a
#    longitude, a point-of-interest category, and a name
let RawPOI? = VecKC[Lat?, Lon?, Cat?, Name?]

### Contract Helpers ###

# ListC[T] is a list of `T`s (linear time):
let ListC = Cons.ListC
# List of unspecified element type (constant time):
let List? = Cons.list?


interface TRIP_PLANNER:

    # Returns the positions of all the points-of-interest that belong to
    # the given category.
    def locate_all(
            self,
            dst_cat:  Cat?           # point-of-interest category
        )   ->        ListC[RawPos?] # positions of the POIs

    # Returns the shortest route, if any, from the given source position
    # to the point-of-interest with the given name.
    def plan_route(
            self,
            src_lat:  Lat?,          # starting latitude
            src_lon:  Lon?,          # starting longitude
            dst_name: Name?          # name of goal
        )   ->        ListC[RawPos?] # path to goal

    # Finds no more than `n` points-of-interest of the given category
    # nearest to the source position.
    def find_nearby(
            self,
            src_lat:  Lat?,          # starting latitude
            src_lon:  Lon?,          # starting longitude
            dst_cat:  Cat?,          # point-of-interest category
            n:        nat?           # maximum number of results
        )   ->        ListC[RawPOI?] # list of nearby POIs

struct pos:
    let lat:Lat?
    let lon:Lon?
   
struct cat_and_name:
    let cat:Cat?
    let name:Name?

struct node:
    let pos:pos?
    let POILL: OrC(NoneC, OrC(ListC[cat_and_name?], cat_and_name?))
    
struct route:
    let distance: num?
    let directions: ListC[pos?]
    
struct travel:
    let pos: pos?
    let dist:num?
    

class TripPlanner (TRIP_PLANNER):
    let _map
    
    let _posn_to_index
    let _index_to_node

    def _road_len(self, x:pos?, y:pos?):
        return ((x.lat-y.lat)**2 + (x.lon-y.lon)**2)**(1/2)

    def __init__(self, raw_road_segs: VecC[RawSeg?], raw_POIs: VecC[RawPOI?]):
        let road_segs = [[pos(seg[0], seg[1]), pos(seg[2], seg[3])] for seg in raw_road_segs]
        let POIs = [node(pos(poi[0],poi[1]),cat_and_name(poi[2],poi[3])) for poi in raw_POIs]
        ### MAPPPPPPPINGGGGGGGG#########
        self._posn_to_index = HashTable(2*raw_road_segs.len(), make_sbox_hash())
        self._index_to_node = [None; 2*raw_road_segs.len()]
        for i, el in road_segs:
            for j, posn in el:
                self._posn_to_index.put(posn, 2*i+j)#put them all in
                
        for el in road_segs:# set posns to nodes with empty POI Linked Lists
            for posn in el:
                self._index_to_node[self._posn_to_index.get(posn)] = node(posn, None)
                
        for POI in POIs:#put the pois into the index to node
            let index = self._posn_to_index.get(POI.pos)
            self._index_to_node[index].POILL = cons(POI.POILL ,self._index_to_node[index].POILL)
                            
        ##########GRRRRRRRRRRAAAAAAAAAPPPPPPHHHHHHHHHHIIIIINGGGGGGGGGGGG##################
        self._map = WUGraph(self._index_to_node.len())
        for seg in road_segs:
            let start = self._posn_to_index.get(seg[0])
            let dest = self._posn_to_index.get(seg[1])
            self._map.set_edge(start, dest, self._road_len(seg[0],seg[1]))
        
    def print_me(self):
        print("forward mapper: %p\n backward mapper: %p", self._posn_to_index, self._index_to_node)
        
    def _contains(self, lst, target):
        let copy = lst
        while copy != None:
            let curr = copy.data
            if curr == target:
                return True
            copy = copy.next
        return False
    
    def locate_all(self, dst_cat):
        let return_list = None
        for el in self._index_to_node:
            if node?(el):
                let looper = el.POILL
                while looper != None:
                    if looper.data.cat == dst_cat and not self._contains(return_list, [el.pos.latel.pos.lon]):
                        return_list = cons([el.pos.lat, el.pos.lon], return_list)
                    looper = looper.next
        return return_list
                    
      
    def plan_route(self,src_lat:  Lat?,src_lon:  Lon?,dst_name: Name?)->ListC[RawPos?]:
        let return_list = None
        def dijkstras(start):
            let dist = [[inf, -1]; self._map.n_vertices()]# infinite distance with the previous node = -1 (bc 0 can be node
            let visited = [None; self._map.n_vertices()]# imoprtant bc we can add a distance to something but not have the fastest path to it. Dijkstras means that every node we "visit" will b e the last time we visit it
            dist[start] = [0,start] # setting the distance to start = 0 and the previous node = itself
            let heap = BinHeap(self._map.n_vertices(), lambda a, b: a[0] < b[0])#priority queue shortest path lengths from node im on
            heap.insert([0, start])
            while heap.len()>0:
                let curr = heap.find_min()# smallest path length from current node
                heap.remove_min()
                let curr_v = curr[1] #current vertex
                if not visited[curr_v]:
                    visited[curr_v] = True
                    let neighbor = self._map.get_adjacent(curr_v) #LL of neighbors
                    while neighbor != None:
                        let new_dist = dist[curr_v][0] + self._map.get_edge(curr_v, neighbor.data) #current distance to get there + distance to get to next place based on graph's edge lengths
                        if new_dist < dist[neighbor.data][0]:
                            dist[neighbor.data] = [new_dist, curr_v]
                            heap.insert([new_dist,neighbor.data])
                        neighbor = neighbor.next
            return dist
        let start = self._posn_to_index.get(pos(src_lat, src_lon))
        let dist = dijkstras(start)
        
        let dst = None
        for i, el in self._index_to_node:
            if node?(el):
                let looper = el.POILL
                while looper != None:
                    if looper.data.name == dst_name: dst = i
                    looper = looper.next
                    
        if dst == None or dist[dst][0] == inf: return None
        
        let temp = dst
        while temp != start:
            let el = self._index_to_node[temp].pos
            return_list = cons([el.lat,el.lon], return_list)
            temp = dist[temp][1]
        let start_el = self._index_to_node[start].pos
        return_list = cons([start_el.lat, start_el.lon], return_list)
        return return_list
        
    def find_nearby(self,src_lat:Lat?,src_lon:Lon?,dst_cat:Cat?,n:nat?)->ListC[RawPOI?]:
       let return_list = None
       def dijkstras(start):
           let dist = [inf; self._map.n_vertices()]
           let visited = [None; self._map.n_vertices()]
           dist[start] = 0
           let heap = BinHeap(self._map.n_vertices(), lambda a, b: a[0] < b[0])
           heap.insert([0, start])
           while heap.len()>0:
               let curr = heap.find_min()
               heap.remove_min()
               let curr_v = curr[1]
               if not visited[curr_v]:
                   visited[curr_v] = True
                   let neighbor =self._map.get_adjacent(curr_v)
                   while neighbor != None:
                       let new_dist = dist[curr_v] + self._map.get_edge(curr_v, neighbor.data)
                       if new_dist < dist[neighbor.data]:
                           dist[neighbor.data] = new_dist
                           heap.insert([new_dist,neighbor.data])
                       neighbor = neighbor.next
           return dist
           
       # Rank all dst_cat by dist   
       let dist = dijkstras(self._posn_to_index.get(pos(src_lat, src_lon)))
       let heap = BinHeap(self._map.n_vertices(), lambda a, b: a[0] < b[0])
       for i, el in self._index_to_node:
           if node?(el):
               let looper = el.POILL
               while looper != None: 
                   if looper.data.cat == dst_cat:
                       heap.insert([dist[i], [el.pos.lat, el.pos.lon, looper.data.cat, looper.data.name]])
                   looper = looper.next
       
       #get fisrt n dst_cats
       let temp = 0
       while heap.len() > 0 and temp < n:       
           let min_item  = heap.find_min()
           heap.remove_min()
           if min_item [0] != inf:
               return_list = cons(min_item[1], return_list)
               temp = temp + 1
       return return_list
                   
def my_first_example():
    return TripPlanner([[0,0, 0,1], [0,0, 1,0]],
                       [[0,0, "bar", "Hopleaf"],
                        [0,1, "food", "Gigio's"]])
                        
def my_second_example():
    return TripPlanner(
        [[0,0, 1,0], [1,0, 2,0], [2,0, 3,0], [3,0, 4,0],
         [0,1, 1,1], [1,1, 2,1], [2,1, 3,1], [3,1, 4,1],
         [0,2, 1,2], [1,2, 2,2], [2,2, 3,2],
         [1,3, 2,3], [2,3, 3,3], [3,3, 4,3],
         [0,4, 1,4], [1,4, 2,4],
         [0,0, 0,1], [0,1, 0,2], [0,2, 0,4],
         [1,0, 1,1], [1,1, 1,2], [1,2, 1,3], [1,3, 1,4],
         [2,0, 2,1], [2,1, 2,2], [2,2, 2,3], [2,3, 2,4],
         [3,0, 3,1], [3,1, 3,2], [3,2, 3,3],
         [4,0, 4,1], [4,1, 4,3],
         [0,2, 1,3]],
        [[0,0, "hotel",    "Grand Inn"],
         [0,0, "food",    "Grand Inn's Breakfast House"],
         [2,0, "cafe",     "Morning Brew"],
         [4,0, "food",     "Noodle House"],
         [1,1, "museum",   "City Museum"],
         [3,1, "cafe",     "Beanery"],
         [4,1, "food",     "Taco Stand"],
         [0,2, "park",     "Riverside Park"],
         [2,2, "pharmacy", "MedPlus"],
         [3,2, "museum",   "Art Gallery"],
         [1,3, "food",     "Burger Joint"],
         [4,3, "hotel",    "Harbor Hotel"],
         [0,4, "park",     "Sunset Park"],
         [2,4, "pharmacy", "QuickCare"]])
         
def test_me():
    test 'My first locate_all test':
        assert my_first_example().locate_all("food") == \
            cons([0,1], None)
        
    test 'My second locate_all test':
        assert my_second_example().locate_all("food") == cons {data: [1, 3], next: cons {data: [4, 1], next: cons {data: [4, 0], next: cons {data: [0, 0], next: None}}}}

    test 'My first plan_route test':
        assert my_first_example().plan_route(0, 0, "Gigio's") == \
            cons([0,0], cons([0,1], None))

    test 'My first find_nearby test':
        assert my_first_example().find_nearby(0, 0, "food", 1) == \
            cons([0,1, "food", "Gigio's"], None)
        
    test 'My second find_nearby test':
        assert my_second_example().find_nearby(0, 0, "food", 1) == \
            cons([0,0, "food", "Grand Inn's Breakfast House"], None)