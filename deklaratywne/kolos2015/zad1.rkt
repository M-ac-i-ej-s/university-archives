#lang scheme 

(define (delete x l)
  (foldl (lambda (element acc)
               (if (eq? element x)
                   acc
                   (cons element acc)))
             '()
             l))

(display (delete 5 '(1 2 3 4 5 2)))            