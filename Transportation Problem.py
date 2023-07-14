import sys
import util
sys.setrecursionlimit(10000)

### Model (search problem)

class TransportationProblem(object):
    def __init__(self, N):
        # N = number of blocks
        self.N = N
    def startState(self):
        return 1
    def isEnd(self, state):
        return state == self.N
    def succAndCost(self, state):
        # return list of (action, newState, cost) triples
        result = []
        if state+1<=self.N:
            result.append(('walk', state+1, 1))
        if state*2<=self.N:
            result.append(('tram', state*2, 2))
        return result

### Algorithms

def printSolution(solution):
    totalCost, history = solution
    print('totalCost: {}'.format(totalCost))
    for item in history:
        print(item)

def DFS(problem):
    stack = [(problem.startState(), [], 0)]
    while stack:
        state, path, totalCost = stack.pop()
        if problem.isEnd(state):
            return (totalCost, path)
        for action, newState, cost in problem.succAndCost(state):
            stack.append((newState, path + [(action, newState, cost)], totalCost+cost))

def aStarSearch(problem, heuristic):
    frontier = util.PriorityQueue()
    frontier.update(problem.startState(), heuristic(problem.startState(), problem.N))
    while True:
        state, pastCost = frontier.removeMin()
        if problem.isEnd(state):
            return (pastCost, [])

        for action, newState, cost in problem.succAndCost(state):
            totalCost = pastCost + heuristic(newState, problem.N) + cost # Add the heuristic cost to the total cost
            frontier.update(newState, totalCost)

def manhattan_distance(state1, state2):
    return abs(state1 - state2)

### Main

problem = TransportationProblem(N=40)
print("\nDepth First Search: ")
printSolution(DFS(problem))
print("\nA* Search: ")
printSolution(aStarSearch(problem, manhattan_distance))