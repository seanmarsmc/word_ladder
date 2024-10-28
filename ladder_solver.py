import collections

WORD_FILE = "many_words.txt"

def ladder_solver():
    start = input("Enter the start word: ").strip()
    end = input("Enter the end word: ").strip()
    possible_words = get_words(WORD_FILE)
    length,path = ladder_length(start,end,possible_words)
    print_path(length,path)

def print_path(length,path):
    print(length-1,end=" ")
    for idx, word in enumerate(path):
        print(word, end="")
        if idx != len(path) - 1:
            print(" -> ", end="")
        else:
            print()

def ladder_length(start:str,dest:str,possible_words:list):
    if len(start) != len(dest):
        return -1, []
    if dest not in possible_words:
        return -1, []

    neighbors = collections.defaultdict(list) 
    for word in possible_words:
        if len(word) != len(start):
            continue
        for idx in range(len(word)):
            pattern = word[:idx] + "." + word[idx+1:]
            neighbors[pattern].append(word)
    
    visit = set([start])
    deque = collections.deque([(start)])
    res = 1
    predecessors = {start: None}

    while deque:
        for idx in range(len(deque)):
            word = deque.popleft()
            if word == dest:
                path = []
                while word:
                    path.append(word)
                    word = predecessors[word]
                return res, path[::-1]
            for jdx in range(len(word)):
                pattern = word[:jdx] + "." + word[jdx+1:]
                for neighbor in neighbors[pattern]:
                    if neighbor not in visit:
                        visit.add(neighbor)
                        deque.append(neighbor)
                        predecessors[neighbor] = word
        res += 1

    return -1, []

# SETUP
def get_words(fn):
    with open(fn,"r") as file:
        return file.read().splitlines()

if __name__ == "__main__":
    ladder_solver()
