import math

# Node class
class Node:
    def __init__(self, name, cost=0, is_and_node=False):
        self.name = name
        self.cost = cost
        self.is_and_node = is_and_node
        self.children = []
        self.solved = False
        self.solution_cost = math.inf

    def add_child(self, child_node):
        self.children.append(child_node)

# AO* Algorithm
def ao_star(node):
    if node.solved:
        return node.solution_cost

    if not node.children:
        node.solved = True
        node.solution_cost = node.cost
        return node.cost

    if not node.is_and_node:
        min_cost = math.inf
        for child in node.children:
            child_cost = ao_star(child)
            if child_cost < min_cost:
                min_cost = child_cost
        node.solution_cost = node.cost + min_cost
        node.solved = True
        return node.solution_cost
    else:
        total_cost = node.cost
        all_children_solved = True
        for child in node.children:
            child_cost = ao_star(child)
            if child_cost == math.inf:
                all_children_solved = False
            total_cost += child_cost
        if all_children_solved:
            node.solution_cost = total_cost
            node.solved = True
            return node.solution_cost
        else:
            return math.inf

# Function to display the graph structure
def display_graph_structure(node, indent=""):
    node_type = "AND" if node.is_and_node else "OR"
    print(f"{indent}├── {node.name} (Cost: {node.cost}, Type: {node_type})")
    for i, child in enumerate(node.children):
        if i == len(node.children) - 1:
            display_graph_structure(child, indent + "    ")
        else:
            display_graph_structure(child, indent + "│   ")

# Setup the ITS system
def setup_system():
    # Create nodes
    root = Node("Root", cost=0, is_and_node=False)
    solve_equations = Node("Solve Equations", cost=5, is_and_node=True)
    understand_functions = Node("Understand Functions", cost=4, is_and_node=True)
    practice_equations = Node("Practice Equations", cost=3)
    learn_operations = Node("Learn Operations", cost=2)
    graph_functions = Node("Graph Functions", cost=3)

    # Define AND-OR relationships
    root.add_child(solve_equations)
    root.add_child(understand_functions)
    solve_equations.add_child(practice_equations)
    solve_equations.add_child(learn_operations)
    understand_functions.add_child(graph_functions)

    return {
        "Root": root,
        "Solve Equations": solve_equations,
        "Understand Functions": understand_functions,
        "Practice Equations": practice_equations,
        "Learn Operations": learn_operations,
        "Graph Functions": graph_functions
    }

# Main function to run the ITS
if __name__ == "__main__":
    nodes = setup_system()

    # Display the entire graph structure
    print("Entire graph structure:")
    display_graph_structure(nodes["Root"])

    # Get user input
    user_goals = input("\nEnter the learning goals (comma-separated, e.g., 'Solve Equations, Understand Functions'): ").strip().split(", ")

    # Process each learning goal
    for goal in user_goals:
        goal = goal.strip()
        if goal in nodes:
            print(f"\nGraph structure for learning goal '{goal}':")
            display_graph_structure(nodes[goal])
            min_cost = ao_star(nodes[goal])
            print(f"\nMinimum cost to achieve '{goal}': {min_cost}")
        else:
            print(f"\nLearning goal '{goal}' not recognized. Please enter a valid goal.")
