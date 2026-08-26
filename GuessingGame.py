# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 16:56:14 2026


I include a txt file with the submission that save the binary tree from my playtest so it can read from it next session.
I used it to save time from having to type in the same questions and answers over and over.
"""


#Do a binary node
class Node:
    def __init__(self, data, isQuestion = False):
        self.data = data
        self.isQuestion = isQuestion
        self.yes = None
        self.no = None
        
def Ask(node):
    answer = input("What are you thinking of? ").lower()
    question = input(f"Please enter a question that differentiates a {node.data} from a {answer}: ")
    ansQuestion = input(f"Is the answer for {answer} yes or no (Y/N): ").lower()
    
    old_data = node.data
    #Turn current node into a question node
    node.data = question
    node.isQuestion = True
    
    #Paste the answer and the old answer in this node into the respective y/n answer for the question provided
    if ansQuestion == "y":
        node.yes = Node(answer)
        node.no = Node(old_data)
    elif ansQuestion == "n":
        node.no = Node(answer)
        node.yes = Node(old_data)

def Play(node):
    
    if not node.isQuestion:
        print(f"You are thinking of a {node.data}.")
        answer = input("Am I right (Y/N)? ").lower()
        
        if answer == "y":
            print("Computer won.")
        elif answer == "n":
            print("Computer lost.")
            Ask(node)
        
    else: 
        print("I'm going to try to guess what you are thinking of.")
        
        answer = input(node.data + " ").lower()
        
        if answer == "n":
            Play(node.no)
        if answer == "y":
            Play(node.yes)


#Program saves the tree in a text file so that it can be loaded next time. 
#The format is Q for question and A for answer, each on a new line.
def WriteTree(node, file):
    if node.isQuestion:
        file.write("Q" + node.data + "\n")
        WriteTree(node.yes, file)
        WriteTree(node.no, file)
    else:
        file.write("A" + node.data + "\n")


def LoadTree(dataIterator):
    try:
        line = next(dataIterator).strip()
    except StopIteration:
        print("The tree is not a full binary tree. But nothing serious.")
        
    if line.startswith("Q"):
        node = Node(line[1:], isQuestion = True)
        #Read yes first then no because I write yes before no
        node.yes = LoadTree(dataIterator)
        node.no = LoadTree(dataIterator)
        return node
    else:
        node = Node(line[1:], isQuestion = False)
        return node
    
    



if __name__ == "__main__":
    
    print("Guessing game!")
    
    root = Node("table")
    
    a = input("Do you want to load your progress (Y/N)? ").lower()
    if a == "y":
        try:
            with open("GuessingTreeData.txt", "r") as file:
                lines = file.readlines()
                if not lines:
                    print("File empty. use default root node.")
                    root = Node("table")
                else:
                    dataIterator = iter(lines)
                    root = LoadTree(dataIterator)
        except FileNotFoundError:
            print("Found no progress file. Start with default root node.")
            root = Node("table")
    elif a == "n":
        root = Node("table")
    
    while True:
        
        Play(root)
        
        again = input("Do you want yo play again (Y/N): ").lower()
        if again == "y":
            print("\nPlay again\n")
        else: 
            with open("GuessingTreeData.txt", "w") as file:
                WriteTree(root,file)
            
            break
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
