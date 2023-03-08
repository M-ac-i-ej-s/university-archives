#lang racket

(define (is-even? n)
  (if (even? n)
      #t
      #f))

(define (is-odd? n)
  (if (odd? n)
      #t
      #f))

(define (same-value? p1 p2 x y)
  (if (and (p1 x y) (p2 x y))
    #t
    #f))

(display (same-value? + * 2 2 ))          