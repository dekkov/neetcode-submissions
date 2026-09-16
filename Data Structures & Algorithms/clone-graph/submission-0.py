from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # original node -> cloned node
        nodeToCopy = {
            node: Node(node.val)
        }

        q = deque([node])

        while q:
            curr = q.popleft()

            for nei in curr.neighbors:
                # First time seeing this node:
                # create its clone and visit it later.
                if nei not in nodeToCopy:
                    nodeToCopy[nei] = Node(nei.val)
                    q.append(nei)

                # Connect curr's clone to neighbor's clone.
                nodeToCopy[curr].neighbors.append(nodeToCopy[nei])

        return nodeToCopy[node]