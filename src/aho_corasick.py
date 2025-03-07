from typing import List, Dict, Tuple, Optional
from collections import deque

class TrieNode:
    """
    Node representation for the Aho-Corasick algorithm.
    
    Attributes:
        children (dict): Dictionary of child nodes
        failure_link (Optional[TrieNode]): Failure link to another node
        output (Optional[str]): Pattern if this is the end of a pattern
        is_end (bool): Whether this node represents the end of a pattern
    """
    def __init__(self):
        self.children = {}
        self.failure_link = None
        self.output = None
        self.is_end = False

class AhoCorasick:
    """
    Implements the Aho-Corasick algorithm for efficient multiple string matching.
    
    The Aho-Corasick algorithm allows for simultaneous matching of multiple 
    patterns in a given text with linear time complexity.
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
        
        # Initialize root node
        self.root = TrieNode()
        
        # Build the trie with sorted patterns to handle overlapping matches
        sorted_patterns = sorted(patterns, key=len, reverse=True)
        for pattern in sorted_patterns:
            self._add_pattern(pattern)
        
        # Construct failure links
        self._build_failure_links()
    
    def _add_pattern(self, pattern: str):
        """
        Add a pattern to the trie.
        
        Args:
            pattern (str): Pattern to add to the trie
        """
        node = self.root
        for char in pattern:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        # Mark end of pattern and store the full pattern
        node.is_end = True
        node.output = pattern
    
    def _build_failure_links(self):
        """
        Construct failure links using BFS.
        """
        # Initialize queue for BFS
        queue = deque()
        
        # Set initial failure links for root's direct children
        for char, child in self.root.children.items():
            child.failure_link = self.root
            queue.append(child)
        
        # BFS to build failure links
        while queue:
            current_node = queue.popleft()
            
            # Iterate through current node's children
            for char, child in current_node.children.items():
                queue.append(child)
                
                # Find failure link
                failure_candidate = current_node.failure_link
                while failure_candidate:
                    if char in failure_candidate.children:
                        child.failure_link = failure_candidate.children[char]
                        break
                    failure_candidate = failure_candidate.failure_link
                
                # If no suitable failure link found, point to root
                if child.failure_link is None:
                    child.failure_link = self.root
    
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
        
        # Iterate through all possible starting points
        for start in range(len(text)):
            current_node = self.root
            
            # Search from this starting point
            for i in range(start, len(text)):
                char = text[i]
                
                # Move to next state or follow failure links
                while current_node and char not in current_node.children:
                    current_node = current_node.failure_link
                    if current_node is None:
                        current_node = self.root
                        break
                
                # Follow transition if possible
                if current_node and char in current_node.children:
                    current_node = current_node.children[char]
                else:
                    current_node = self.root
                
                # Check for matches
                state = current_node
                while state and state != self.root:
                    if state.is_end:
                        pattern = state.output
                        matches.append((start, pattern))
                    
                    # Follow failure link
                    state = state.failure_link
        
        # Remove duplicates while preserving order
        unique_matches = []
        seen = set()
        for match in matches:
            if match not in seen:
                unique_matches.append(match)
                seen.add(match)
        
        return unique_matches