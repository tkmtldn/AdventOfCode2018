class Node:
    def __init__(self, value, prevNode=None, nextNode=None):
        self.value = value
        self.prev = prevNode
        self.next = nextNode

max_players = 458
max_marbles = 72019*100

marbles = Node(0)
marbles.prev = marbles
marbles.next = marbles

position = marbles
results = {}

for points in range(1, max_marbles+1):
    if points % 23 == 0:
        player = (points % max_players) + 1
        position = position.prev.prev.prev.prev.prev.prev.prev
        results[player] = results.get(player, 0) + points + position.value
        position.prev.next = position.next
        position = position.next
    else:
        new = Node(points, position.next, position.next.next)
        position.next.next.prev = new
        position.next.next = new
        position = new

print(max(results.values()))