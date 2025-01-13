graph = {
     'A' : ['B','C'],
     'B' : ['D', 'E'],
     'C' : ['F'],
     'D' : [],
     'E' : [],
     'F' : []
}

start = 'A'
goal = 'E'

frontier = [start]
explored = set()

while len(frontier) > 0:
     current = frontier.pop()
     print('Current:', current)

     if current == goal:
          print('Found' , goal)
          break

     for node in graph[current]:
               frontier.append(node)