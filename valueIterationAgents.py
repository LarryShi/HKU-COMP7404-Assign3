import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0

        # Write value iteration code here
        
        "*** YOUR CODE HERE ***"
        states = mdp.getStates()
        #for state in states:
          #print(state)
          #print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<,")
    
        #print mdp.getTransitionStatesAndProbs(state, action)
        #print mdp.getReward(state, action, nextState)
        #print mdp.isTerminal(state)
      
        #print("Discout:",discount)
        i=0
        while i < iterations:
          newValues = self.values.copy()
          i+=1
          for state in states:
            stateValue=None
            actions = mdp.getPossibleActions(state)

            for action in actions:
              newStateValue=self.getQValue(state,action)
              if stateValue==None or newStateValue > stateValue:
                stateValue=newStateValue
            
            if stateValue == None:
              newValues[state]=0
            else:
              newValues[state]=stateValue

          self.values=newValues

          #print(self.values)


    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        value = 0
        transitions = self.mdp.getTransitionStatesAndProbs(state,action)
        for nextState, probability in transitions:
          value += probability * (self.mdp.getReward(state, action, nextState) + (self.discount * self.values[nextState]))

        return value
        util.raiseNotDefined()

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        potentialActions = self.mdp.getPossibleActions(state)

        if len(potentialActions)==0:
          return None

        value=None
        choosedAction=None
        for action in potentialActions:
          tmpValue=self.getQValue(state, action)
          
          if value==None or tmpValue>value:
            value=tmpValue
            choosedAction=action

        return choosedAction

        util.raiseNotDefined()

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
