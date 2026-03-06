#lang htdp/asl
;---------------------------Q1-----------------------------------;
(define (filter-map function predicate lst)
  (if (empty? lst) (list) (if (predicate (first lst)) (cons (function (first lst)) (filter-map function predicate (rest lst))) (filter-map function predicate (rest lst)))))
;----------------------------------------------------------------;
(check-expect (filter-map (lambda (x) (* x x)) odd? (list 1 2 3)) (list 1 9))
;--------------------------Q2------------------------------------;
(define (lookup char dict)
   (if (empty? (filter (lambda (x) (equal? (first x) char)) dict)) "unbound" (apply second (filter (lambda (x) (equal? (first x) char)) dict))))
;----------------------------------------------------------------;
(define sample-dictionary
(list (list "a" 1)
(list "b" 2)
(list "+" +)
(list "-" -)
(list "*" *)
(list "/" /)))
;----------------------------------------------------------------;
(check-expect (lookup "a" sample-dictionary) 1)
(check-expect (lookup "x" sample-dictionary) "unbound")
;-------------------------Q3-------------------------------------;
(define (execute expression dict)
  (cond [(string? expression) (lookup expression dict)]
        [(number? expression) expression]
        [(boolean? expression) expression]
        [(list? expression)
         (apply (execute (first expression) dict) (map (lambda (x) (execute x dict)) (rest expression)))]))
;----------------------------------------------------------------;
(define a-list-expression
'("*" ("+" 1 "a") "b"))
;----------------------------------------------------------------;
(check-expect (execute 1 sample-dictionary) 1)
(check-expect (execute "b" sample-dictionary) 2)
(check-expect (execute '("+" 1 2) sample-dictionary) 3)
(check-expect (execute a-list-expression sample-dictionary) 4)
;-------------------------Q4-------------------------------------;
(define (repeat-while test body)
    (when (test) (begin (body) (repeat-while test body))))
;----------------------------------------------------------------;
(check-expect (begin (repeat-while (λ () false)
                                   (λ () (error "This code should never run!")))
                     "It didn't break")
              "It didn't break")
(check-expect (local [(define sum 0)
                      (define counter 1)]
                (begin (repeat-while (λ () (<= counter 10))
                                     (λ () (begin (set! sum (+ sum counter))
                                                  (set! counter (+ counter 1)))))
                       sum))
              (+ 1 2 3 4 5 6 7 8 9 10))
;-------------------------Q5-------------------------------------;

(define (sum-numbers lst)
  (local[(define sum 0)
         (define new-lst lst)]
  (begin
   (repeat-while (lambda () (not(empty? new-lst))) (lambda () (begin
                                                           (set! sum (+ (first new-lst) sum))
                                                           (set! new-lst (rest new-lst)))))
   sum)))

(check-expect (sum-numbers (list 1 2 3)) 6)
