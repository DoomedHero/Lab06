# Step 5: Create a MindMapLeaf object and test the __str__ and display methods.

from Mindmap_Leaf import MindMapLeaf

leaf = MindMapLeaf("Jean-Luc Picard", "circle")
print(str(leaf))  # Should display "((Jean-Luc Picard))"
leaf.display(2)   # Should display "  ((Jean-Luc Picard))" with two spaces

print("MindMapLeaf tests completed!")

# Step 6: Create MindMapComposite and MindMapLeaf objects to test
root = MindMapComposite("Root", "circle")
leaf1 = MindMapLeaf("Child 1", "square")
leaf2 = MindMapLeaf("Child 2", "cloud")
root.add(leaf1)
root.add(leaf2)

print(str(root))  # Should display "((Root))"
root.display()    # Should display root and its children

print("MindMapComposite tests completed!")