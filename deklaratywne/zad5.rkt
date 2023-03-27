#lang racket

(define (square-list l)
  (map (lambda (x) (* x x)) l))

(square-list '(1 2 3))