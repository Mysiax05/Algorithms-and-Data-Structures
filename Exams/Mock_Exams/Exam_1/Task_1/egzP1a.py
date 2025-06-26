from egzP1atesty import runtests 

def titanic(W, M, D):
    target_morse = ''.join(M[ord(letter) - ord('A')][1] for letter in W)
    
    available_morse = [M[idx][1] for idx in D]
    
    from collections import deque
    queue = deque()
    queue.append(('', 0))
    visited = set()
    visited.add('')
    
    while queue:
        current_morse, steps = queue.popleft()
        
        if current_morse == target_morse:
            return steps
        
        for code in available_morse:
            new_morse = current_morse + code
            if new_morse in visited:
                continue
            if not target_morse.startswith(new_morse):
                continue
            if len(new_morse) > len(target_morse):
                continue
            visited.add(new_morse)
            queue.append((new_morse, steps + 1))

runtests ( titanic, recursion=False )