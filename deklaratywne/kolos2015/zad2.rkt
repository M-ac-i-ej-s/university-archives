#lang scheme

(define (count x l)
    (foldl (lambda (el acc)
        (if (equal? el x)
            (+ acc 1)
            acc))
            0
            l))

(display (count 3 '(2 2 2 3 4 3)))