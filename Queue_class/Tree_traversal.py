#================================================================================
"""
재귀호출로 인해 작동되는 방식!
inorder를 예시로 살펴보자
        A
      / \
    B   C
   / \
 D   E

"""

#================================================================================

def inorder(node):
    if node:
        inorder(node.left)    # 왼쪽 먼저 - 여기서 완전히 끝날 때까지 기다림!
        print(node.data)      # 위 줄이 완전히 끝난 후 실행
        inorder(node.right)   # 위 줄이 끝난 후 실행

    inorder(A) 호출
        inorder(A.left) = inorder(B) 호출 [ 아직 A는 출력안함]
            inorder(B.left) = inorder(D) 호출 [ 아직 B 출력 안함]
                inorder(D.left) = inorder(None) -> 아무것도 안함
                print(D) 실행
                inorder(D.right) = inorder(None) -> 아무것도 안함


"""   
    inorder(A) 호출
    ├─ inorder(A.left) = inorder(B) 호출 [아직 A 출력 안함!]
           ├─ inorder(B.left) = inorder(D) 호출 [아직 B 출력 안함!]
                              ├─ inorder(D.left) = inorder(None) → 아무것도 안함
                              ├─ print("D") 실행 ✓
                              └─ inorder(D.right) = inorder(None) → 아무것도 안함
           ├─ print("B") 실행 ✓ [이제서야 B가 출력됨]
           └─ inorder(B.right) = inorder(E) 호출
                              ├─ inorder(E.left) = inorder(None) → 아무것도 안함
                              ├─ print("E") 실행 ✓
                              └─ inorder(E.right) = inorder(None) → 아무것도 안함
    ├─ print("A") 실행 ✓ [이제서야 A가 출력됨]
    └─ inorder(A.right) = inorder(C) 호출
       ├─ inorder(C.left) = inorder(None) → 아무것도 안함
       ├─ print("C") 실행 ✓
       └─ inorder(C.right) = inorder(None) → 아무것도 안함
"""