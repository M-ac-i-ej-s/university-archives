#lang racket

(define (product term next b)
  (if (> b 0)
      (* (term b) (product term next (- b 1)))
      1))

(define (silnia n)
  (define (next i) (+ i 1))
  (define (identity x) x)
  (product identity next n)
)       

(define (numer k)
  (if (even? k) k (+ k 1)))

(define (denom k)
  (+ k 2))

(define (pi-approximation n)
  (* 4 (/ (product numer identity n) (product denom identity n))))  

(display (silnia 5 ))           

(display (pi-approximation 5))
          