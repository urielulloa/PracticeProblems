;Binary Search Tree implementation in Scheme.
;A tree is a list where the car value is the current value, the cadr is the left subtree, and the caddr is the right subtree.

(define (make-bst n left right) ;makes a Binary Search Tree
   (list n left right)) ;n is the root, left subtree, and right-subtree

(define empty-bst '()) ;an empty tree is just an empty list

(define (flatten x)   ;removes parenthesis
  (cond ((null? x) x)
  ((atom? x)(list x))
  (else (append(flatten (car x))
  (flatten (cdr x))))))

(define (traverse bst) ;returns the values stored in the BST
  (if (null? bst) ;if the tree is empty
    '() ;return empty list
    (flatten (cons (cons  ;we will need to combine 3 lists (left, root, and right) then flatten it.
    (traverse (cadr bst)) ;start with the left side of the tree
    (car bst)) ;take the root of the tree
    (traverse (caddr bst)))))) ;end with the right side of the tree

(define (insert n bst)  ;inserts a new value into the tree
  (cond
    ((null? bst) ;if the tree is empty,
      (make-bst n '() '())) ;make a new tree with the root
    ((= (car bst) n) bst) ;if the value is already in the tree, return the tree.
    ((< n (car bst)) ;if n is less than the current value
      (make-bst (car bst) (insert n (cadr bst)) (caddr bst))) ;insert n into the left tree
    (else
      (make-bst (car bst) (cadr bst) (insert n (caddr bst)))))) ;else n is greater than root so insert n into the right tree

(define (present? n bst) ;sees if the value is present in the tree
  (cond ((null? bst) #f) ;if the tree is empty, return false.
  ((equal? (car bst) n) #t) ;if the root is equal to n, return true.
  ((< n (car bst)) (present? n (cadr bst))) ;else if n is less than the current value, recursively search in the left tree.
  (else (present? n (caddr bst))))) ;else, n is greater than the current value, recursively search in the right tree.
