#lang racket

(define (iter f n)
    (if (= n 0)
        1
        (* f (iter f (- n 1))))
        )

(display (iter 2 3))