#lang htdp/isl+

(require "no_list_procs.rkt")


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;            Fixing Recursion Errors                ;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 3.1. Computing Sum of Squares
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; sum-of-squares-up-to : number -> number
;;   Given a non-negative integer n, compute 1^2 + 2^2 + ... + n^2
(check-expect (sum-of-squares-up-to 3) 14) ;; uncomment this after fixing the error
(define (sum-of-squares-up-to n)
  (if (= n 0)
      0
      (+ (* n n)
         (sum-of-squares-up-to (- n 1)))))


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 3.2. Multiply Everything
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; multiply-everything : (listof number) -> number
;;   Given a list of numbers, compute their product.
(check-expect (multiply-everything (list 3 4 5)) 60)

(define (multiply-everything lst-nums)
  (if (empty? lst-nums)
      1
      (* (first lst-nums) (multiply-everything (rest lst-nums)))))


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 3.3. Finding Zeroes
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; Fill in your test case for is-there-any-zero? here
(define test-3.3 (list 1 1 1 1 0 1 1 1))

;; is-there-any-zero? : (listof number) -> boolean
;;   Given a list of numbers, checks whether there is a zero in it.
(check-expect (is-there-any-zero? empty) #false)
(check-expect (is-there-any-zero? test-3.3) #true)
(define (is-there-any-zero? lst-nums)
  (if (empty? lst-nums)
      #false
      (or (= (first lst-nums) 0)
           (is-there-any-zero? (rest lst-nums)))))




;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;          Part I: Ordinary Recursion               ;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 4.1. Word Concatenation
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; Write your solution for Problem 4.1, concat-words, here
(define (concat-words los)
  (if (empty? los) "" (string-append (first los) ";" (concat-words (rest los)))))
;; concat-words : (listof string) -> string
(check-expect (concat-words (list "the" "lazy" "dog")) "the;lazy;dog;")
(check-expect (concat-words (list)) "")


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 4.2. Total Value of Coin Collection
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; A Coin-collection is a structure: (make-coin-collection Number Number)
(define-struct coin-collection [value count])
;; - `value' is the face value of the coin. It must store a positive number.
;; - `count' is the count of the coin. It must store a non-negative integer.

;; Write your solution for Problem 4.2, total-value, here
(define (total-value locc)
  (cond [(empty? locc) 0]
        [else (+ (* (coin-collection-value (first locc)) (coin-collection-count (first locc))) (total-value (rest locc)))]))
;; total-value : (listof coin-collection) -> number
(check-expect
 (total-value (list (make-coin-collection 10 3)
(make-coin-collection 5 0)
(make-coin-collection 1 2)
(make-coin-collection 0.25 3)))
 32.75)


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 4.3. Lengths of Words
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; Write your solution for Problem 4.3, word-lengths, here
(define (word-lengths los)
  (if (empty? los) '() (append (list(string-length(first los))) (word-lengths (rest los)))))
      
;; word-lengths : (listof string) -> (listof number)
(check-expect (word-lengths (list "the" "perro" "playa" "pee")) (list 3 5 5 3))


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 4.4. Finding Short Words
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; Write your solution for Problem 4.4, find-short-words, here
(define (find-short-words len low)
  (cond [(empty? low) '()]
        [(>= len (string-length(first low))) (append (list (first low)) (find-short-words len (rest low)))]
        [else (find-short-words len (rest low))]))
;; find-short-words : number (listof string) -> (listof string)
(check-expect (find-short-words 3 (list "the" "lazy" "fox" "stewart")) (list "the" "fox"))




;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;         Part II: Iterative Recursion              ;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 5.1. Word Concatenation, Iteratively
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; iterative-concat-words : (listof string) -> string
;;   Takes a list of strings and concatenates them using iterative recursion

(define (iterative-concat-words lst-strs)
  (concat-words-helper lst-strs concat-words-initial-value))

;; Write your solution for Problem 5.1.1, concat-words-initial-value, here
;; concat-words-initial-value is the initial value for iteration in iterative-concat-words
(define concat-words-initial-value
  "")
(check-expect (iterative-concat-words (list "the" "lazy" "dog")) "the;lazy;dog;")
;; Write your solution for Problem 5.1.2, concat-words-helper, here

;; concat-words-helper : (listof string) string -> string
;;   concat-words-helper is the helper function for iterative-concat-words
;;   that concatenates the strings using iterative recursion
(check-expect (iterative-concat-words (list "the" "lazy" "dog")) "the;lazy;dog;")
(check-expect (concat-words (list "the" "lazy" "dog")) "the;lazy;dog;")

(define (concat-words-helper lst-strs acc)
  (cond [(empty? lst-strs) acc]
          [else (concat-words-helper (rest lst-strs) (string-append acc (first lst-strs) ";"))]))


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 5.2. Finding Short Words, Iteratively
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; Write your solution for Problem 5.2.1, find-short-words-helper, here

;; find-short-words-helper : number (listof string) (listof string) -> (listof string)
(check-expect (find-short-words-helper 5 (list "dog") (list "lazy" "the")) (list "the" "lazy" "dog"))

(define (find-short-words-helper num lst acc)
  (cond [(empty? lst) (reverse acc)]
        [(>= num (string-length (first lst))) (find-short-words-helper num (rest lst) (append (list(first lst)) acc))]))
;; Write your solution for Problem 5.2.2, iterative-find-short-words, here


;; iterative-find-short-words : number (listof string) -> (listof string)
(define(iterative-find-short-words num lst)
  (find-short-words-helper num lst '()))



;; DON'T CHANGE EXISTING check-expectS!!!
;; These are just tests to make sure all of your images are named correctly for grading
(check-satisfied test-3.3 list?)
(check-satisfied concat-words procedure?)
(check-satisfied total-value procedure?)
(check-satisfied word-lengths procedure?)
(check-satisfied find-short-words procedure?)
(check-satisfied concat-words-initial-value string?)
(check-satisfied concat-words-helper procedure?)
(check-satisfied find-short-words-helper procedure?)
(check-satisfied iterative-find-short-words procedure?)
