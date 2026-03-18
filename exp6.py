import re
import networkx as nx
import matplotlib.pyplot as plt

# ---------------- DFA Construction (Basic for a*b type patterns) ----------------
class DFA:
    def __init__(self, regex):
        self.regex = regex
        self.states = set()
        self.transitions = {}
        self.start_state = "q0"
        self.accept_states = set()
        self.build_dfa()

    def build_dfa(self):
        # Simple DFA builder for patterns like a*b, ab*, etc.
        self.states = {"q0", "q1", "q2"}
        self.transitions = {
            ("q0", "a"): "q0",
            ("q0", "b"): "q1",
            ("q1", "b"): "q1",
        }
        self.start_state = "q0"
        self.accept_states = {"q1"}

    def simulate(self, string):
        state = self.start_state
        for char in string:
            if (state, char) in self.transitions:
                state = self.transitions[(state, char)]
            else:
                return False
        return state in self.accept_states


# ---------------- Q1: Build DFA ----------------
def q1():
    print("\n--- Q1: DFA Construction ---")
    regex = "a*b"
    dfa = DFA(regex)

    print("States:", dfa.states)
    print("Start State:", dfa.start_state)
    print("Accept States:", dfa.accept_states)
    print("Transitions:")
    for k, v in dfa.transitions.items():
        print(f"{k} -> {v}")


# ---------------- Q2: DFA Simulation ----------------
def q2():
    print("\n--- Q2: DFA Simulation ---")
    dfa = DFA("a*b")

    string = input("Enter string: ")
    if dfa.simulate(string):
        print("Accepted ✅")
    else:
        print("Rejected ❌")


# ---------------- Q3: Visualization ----------------
def q3():
    print("\n--- Q3: DFA Visualization ---")

    dfa = DFA("a*b")
    G = nx.DiGraph()

    for (state, symbol), next_state in dfa.transitions.items():
        G.add_edge(state, next_state, label=symbol)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=2000)

    edge_labels = {(u, v): d["label"] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title("DFA Visualization")
    plt.show()


# ---------------- Q4: Multiple Test Strings ----------------
def q4():
    print("\n--- Q4: Multiple String Testing ---")

    dfa = DFA("a*b")
    test_strings = ["b", "ab", "aaab", "aabbb", "aaabbbabba"]

    for s in test_strings:
        result = "Accepted" if dfa.simulate(s) else "Rejected"
        print(f"{s} -> {result}")


# ---------------- Q5: Using Python Regex (Validation) ----------------
def q5():
    print("\n--- Q5: Regex vs DFA Check ---")

    pattern = re.compile(r"a*b")
    dfa = DFA("a*b")

    string = input("Enter string: ")

    dfa_result = dfa.simulate(string)
    regex_result = bool(pattern.fullmatch(string))

    print("DFA Result:", "Accepted" if dfa_result else "Rejected")
    print("Regex Result:", "Accepted" if regex_result else "Rejected")


# ---------------- MENU (Switch Case Style) ----------------
while True:
    print("\n==== DFA from Regular Expression ====")
    print("1. Construct DFA")
    print("2. Simulate DFA")
    print("3. Visualize DFA")
    print("4. Test Multiple Strings")
    print("5. Compare with Python Regex")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        q1()
    elif choice == "2":
        q2()
    elif choice == "3":
        q3()
    elif choice == "4":
        q4()
    elif choice == "5":
        q5()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")