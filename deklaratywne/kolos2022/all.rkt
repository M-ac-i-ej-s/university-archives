(define (length l)
    (fold-right (lambda (el acc)
               (if (null? l)
                   0
                   (+ acc 1)))
               0
               l))
           
(display (length '(1 2 3 4 5 6)))           

(define (reverse l)
    (fold-right (lambda (el acc)
              (if (null? l)
                    l
                    (append acc (list el))))
              '()
               l))

(display (reverse '(1 2 3 4 5)))      

(define (divisors n)
    (define (for num acc)
         (if (equal? n num)
             (append acc (list num))
             (if (equal? (modulo n num) 0)
                 (for (+ num 1) (append acc (list num)))
                 (for (+ num 1) acc))))
    (for 1 '()))
    

(display (divisors 12))             

(define (take-while p l)
    (define (helper acc ourList)
        (if (p (car ourList))
            (helper (append acc (list (car ourList))) (cdr ourList))
            acc))
    (helper '() l))
               
(display (take-while (lambda (x) (< x 8)) '(4 6 7 8 9)))  