from typing import List, Dict, Tuple
from collections import deque

class AhoCorasick:
    """
    Implements the Aho-Corasick algorithm for efficient multiple string matching.
    
    The Aho-Corasick algorithm allows for simultaneous matching of multiple 
    patterns in a given text with linear time complexity.
    
    Attributes:
        trie (dict): The trie data structure for pattern matching
        fail_links (dict): Failure links for efficient pattern matching
        output_links (dict): Output links to track matched patterns
    """
    
    def __init__(self, patterns: List[str]):
        """
        Initialize the Aho-Corasick automaton.
        
        Args:
            patterns (List[str]): List of patterns to search for
        
        Raises:
            ValueError: If patterns list is empty
            TypeError: If patterns contain non-string elements
        """
        if not patterns:
            raise ValueError("At least one pattern is required")
        
        # Validate input patterns
        if not all(isinstance(p, str) for p in patterns):
            raise TypeError("All patterns must be strings")
        
        # Initialize data structures
        self.trie = {}
        self.fail_links = {}
        self.output_links = {}
        
        # Build the trie
        for pattern in patterns:
            self._add_pattern(pattern)
        
        # Construct failure and output links
        self._build_failure_links()
    
    def _add_pattern(self, pattern: str):
        """
        Add a pattern to the trie.
        
        Args:
            pattern (str): Pattern to add to the trie
        """
        node = self.trie
        for char in pattern:
            node = node.setdefault(char, {})
        node['$'] = pattern  # Mark end of pattern
    
    def _build_failure_links(self):
        """
        Construct failure and output links using BFS.
        """
        # Initialize failure links for root
        queue = deque()
        for char, child in self.trie.items():
            if char != '$':
                self.fail_links[child] = self.trie
                queue.append(child)
        
        # Build failure links
        while queue:
            node = queue.popleft()
            for char, child in node.items():
                if char == '$':
                    continue
                
                queue.append(child)
                
                # Find failure link
                failure_state = self.fail_links.get(node, self.trie)
                while failure_state and char not in failure_state:
                    failure_state = self.fail_links.get(failure_state, None)
                    if failure_state is None:
                        failure_state = self.trie
                
                if failure_state and char in failure_state:
                    self.fail_links[child] = failure_state[char]
                else:
                    self.fail_links[child] = self.trie
    
    def find_all(self, text: str) -> List[Tuple[int, str]]:
        """
        Find all occurrences of patterns in the given text.
        
        Args:
            text (str): Text to search in
        
        Returns:
            List[Tuple[int, str]]: List of (index, pattern) tuples
        
        Raises:
            TypeError: If text is not a string
        """
        if not isinstance(text, str):
            raise TypeError("Text must be a string")
        
        matches = []
        current_node = self.trie
        
        for i, char in enumerate(text):
            # Move to next state
            while current_node and char not in current_node:
                current_node = self.fail_links.get(current_node, None)
                if current_node is None:
                    current_node = self.trie
                    break
            
            # Follow transition if possible
            if current_node and char in current_node:
                current_node = current_node[char]
            else:
                current_node = self.trie
            
            # Check for matches
            state = current_node
            while state:
                if '$' in state:
                    pattern = state['$']
                    # Find all occurrences of this pattern
                    idx = i - len(pattern) + 1
                    matches.append((idx, pattern))
                
                # Follow failure link
                state = self.fail_links.get(state, None)
                if state is None:
                    break
        
        return matches