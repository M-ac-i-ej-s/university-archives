#lang racket

(define (root f a b)
  (let ((fa (f a))
        (fb (f b)))
    (cond ((and (<= fa 0) (> fb 0))
           (half-interval-method f a b))
          ((and (> fa 0) (<= fb 0))
           (half-interval-method f b a))
          (true (error "Function has same sign at endpoints.")))))


(define (half-interval-method f a b &optional tolerance)
  (let* ((tol (or tolerance 0.00001))
         (midpoint (/ (+ a b) 2))
         (fm (f midpoint)))
    (cond ((<= (abs fm) tol) midpoint)
          ((< (* (f a) fm) 0) (half-interval-method f a midpoint tol))
          ((< (* (f b) fm) 0) (half-interval-method f midpoint b tol))
          (true (error "Function is not monotonic.")))))
