#lang scheme

(define (filter pred l)
    (foldl (lambda (el acc)
            (if (pred el)
                (append acc (list el))
                acc))
            '()
            l))

(display (filter list? '((4 3) 7 (1 2 3) 10)))            
        