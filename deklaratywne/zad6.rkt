#lang scheme

(define (make-konto balance)
  (define (withdraw amount)
    (if (< amount balance)
        (begin
          (set! balance (- balance amount))
          balance)
        "Insufficient funds"))
  (define (deposit amount)
    (set! balance (+ balance amount))
    balance)
  (define (check-balance)
    balance)
  (lambda (message . args)
    (cond ((eq? message 'withdraw) (apply withdraw args))
          ((eq? message 'deposit) (apply deposit args))
          ((eq? message 'check-balance) (check-balance))
          (else (error "Unknown message: " message)))))