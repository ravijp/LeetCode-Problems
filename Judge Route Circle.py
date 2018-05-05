# Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

# The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

# Example 1:
# Input: "UD"
# Output: true
# Example 2:
# Input: "LL"
# Output: false

class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        position = [0, 0]
        
        for move in moves:
            if move == 'R':
                position[0] +=1
            elif move == 'L':
                position[0] -=1
            elif move == 'U':
                position[1] += 1
            else:
                position[1] -= 1
        
        if sum(position) == 0:
            return True
        return False
 
#Simple solution
class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        if not moves:
            return True
        
        if moves.count('U')== moves.count('D') and moves.count('L')==moves.count('R'):
            return True
        else:
            return False
