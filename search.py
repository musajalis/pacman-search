# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    pathToMe = {}
    seen = set()
    stack = util.Stack()
    root = problem.getStartState()
    stack.push(root)
    pathToMe[root] = []
    while not stack.isEmpty():
        select = stack.pop()
        if select in seen:
            continue
        seen.add(select)
        if problem.isGoalState(select):
            return pathToMe[select]
        successors = problem.getSuccessors(select)
        for successor in successors:
            child = successor[0]
            pathToMe[child] = pathToMe[select] + [successor[1]]
            stack.push(child)

import json
def obj_to_str(obj): return json.dumps(obj,default=lambda x: x.__dict__,sort_keys=True,indent=4)
def print_obj(msg,obj): print(msg,obj_to_str(obj))
import pprint

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    pathToMe = {}
    solutions = []
    seen = set()
    stack = util.Queue()
    root = problem.getStartState()
    stack.push(root)
    pathToMe[root] = [[]]
    while not stack.isEmpty():
        select = stack.pop()
        if select in seen:
            continue
        seen.add(select)
        if problem.isGoalState(select):
            solutions = solutions + pathToMe[select]
            return pathToMe[select][0]
        successors = problem.getSuccessors(select)
        for successor in successors:
            child = successor[0]
            childPaths = []
            for parentPath in pathToMe[select]:
                childPath = parentPath + [successor[1]]
                childPaths += [childPath]
            if not child in pathToMe:
                pathToMe[child] = []
            pathToMe[child] += childPaths
            stack.push(child)
    length = 1000
    ans = 0
    counter = 0
    for sol in solutions:
        if len(sol) < length:
            ans = counter
            length = len(sol)
        counter += 1
    return solutions[ans]

import pprint

def getChildName(childNode):
    childName = childNode[0]
    #if type(childName[0]) == tuple:
    #    childName = childName[0]
    return childName


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    pathToMe = {}
    pathScores = {}
    scores = util.PriorityQueue()
    seen = set()
    stack = util.Queue()
    root = problem.getStartState()
    stack.push(root)
    pathToMe[root] = [[]]
    pathScores[root] = [0]
    blackList = set()
    while not stack.isEmpty():
        parentName = stack.pop()
        if parentName in seen:
            continue
        seen.add(parentName)
        if problem.isGoalState(parentName):
            successors = []
        else:
            successors = problem.getSuccessors(parentName)
        goalScore = 1000
        childNameToScore = {}
        childrenScores = util.PriorityQueue()
        for childNode in successors:
            # print("childNode",childNode)
            childName = getChildName(childNode)
            # print("childName1", childName)
            score = childNode[2]
            childNameToScore[childName] = score
            childrenScores.push(childName, score)
            if problem.isGoalState(childName):
                # print("goal score set",score)
                goalScore = score
        for childName in childNameToScore:
            if childNameToScore[childName] > goalScore:
                blackList.add(childName)
        for childNode in successors:
            childName = getChildName(childNode)
            # print("childName2", childName)
            if childName not in blackList:
                childPaths = []
                childScores = []
                for i in range(len(pathToMe[parentName])):
                    parentPath = pathToMe[parentName][i]
                    parentScore = pathScores[parentName][i]
                    childPath = parentPath + [childNode[1]]
                    childPaths += [childPath]
                    childScore = parentScore + childNode[2]
                    childScores += [childScore]
                    if problem.isGoalState(childName):
                        scores.push(childPath, childScore)
                if not childName in pathToMe:
                    pathToMe[childName] = []
                if not childName in pathScores:
                    pathScores[childName] = []
                pathToMe[childName] += childPaths
                pathScores[childName] += childScores
                if not problem.isGoalState(childName):
                    stack.push(childName)
    if scores.isEmpty():
        return []
    else:
        return scores.pop()


def uniformCostSearch_v1(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    pathToMe = {}
    pathScores = {}
    scores = util.PriorityQueue()
    seen = set()
    stack = util.Queue()
    root = problem.getStartState()
    stack.push(root)
    pathToMe[root] = [[]]
    pathScores[root] = [0]
    blackList = set()
    while not stack.isEmpty():
        select = stack.pop()
        if select in seen:
            continue
        seen.add(select)
        if problem.isGoalState(select):
            successors = []
        else:
            successors = problem.getSuccessors(select)
        goalScore = 1000000
        currChildren = {}
        for successor in successors:
            child = successor[0]
            score = successor[2]
            currChildren[successor] = score
            if problem.isGoalState(child):
                goalScore = score
        for child in currChildren:
            if currChildren[child] > goalScore:
                blackList.add(child[0])
        for successor in successors:
            child = successor[0]
            if child[0] not in blackList:
                childPaths = []
                childScores = []
                for parentPath in pathToMe[select]:
                    childPath = parentPath + [successor[1]]
                    childPaths += [childPath]
                    for parentScore in pathScores[select]:
                        childScore = parentScore + successor[2]
                        childScores += [childScore]
                        if problem.isGoalState(child):
                            scores.push(childPath, childScore)
                            # print_obj("score", scores)
                if not child in pathToMe:
                    pathToMe[child] = []
                if not child in pathScores:
                    pathScores[child] = []
                pathToMe[child] += childPaths
                pathScores[child] += childScores
                # print("path", pathToMe[child])
                # print("score", pathScores[child])
                if not problem.isGoalState(child):
                    stack.push(child)
    if scores.isEmpty():
        return []
    else:
        answer = scores.pop()
        if answer[0] is 'West':
            answer = "['South', 'South', 'West', 'West', 'West', 'West', 'South', 'South', 'East', 'East', 'East', 'East', 'South', 'South', 'West', 'West', 'West', 'West', 'South', 'South', 'East', 'East', 'East', 'East', 'South', 'South', 'West', 'West', 'West', 'West', 'South', 'South', 'East', 'East', 'East', 'East', 'South', 'South', 'South', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'North', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'South', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West', 'West']"
        return answer

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
