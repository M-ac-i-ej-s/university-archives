#lang scheme

(define (drop-while p l)
  (cond ((and (not (null? l)) (p (car l))) (drop-while p (cdr l)))
        (else l)))