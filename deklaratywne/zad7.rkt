#lang scheme

(define (exchange x y l)
        (foldr (lambda (el acc)
            (if (eq? el x)
                  (cons y acc)
                  (cons el acc)))
            '()
            l))

(display (exchange 2 3 '(1 2 5 5 2 3)))
