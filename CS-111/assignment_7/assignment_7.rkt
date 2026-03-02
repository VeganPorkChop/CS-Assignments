#lang htdp/asl

(require "quiz_lib.rkt")

#|
printf basics

printf (which stands for print formatted)
can be used to print (or produce) a string in the interactions window (the bottom window),
with arguments that are formatted as strings.

For example:

> (printf "this is number ~a\n" 1)
this is number 1

Here, the ~a tells printf, whatever comes after the string, substitute that for ~a, which
is the number 1 in this case

You can use multiple ~a's, as such:

> (printf "numbers ~a, ~a, and ~a!\n" 1 2 3)
numbers 1, 2, and 3!

\n tells printf to create a new line (i.e. a line break):

> (printf "line 1\nline 2\n")
line 1
line 2

|#

;Part 1
;Define the question struct and its methods here.

(define-struct question (text answer points)
  #:methods
  (define show-text (lambda(q)
                      (printf "Q: ~a (~a points)\n" (question-text q)(question-points q))))
  (define check-response (lambda (q r)
                           (equal? r (question-answer q))))
  )


; a question is a ....
; (make-question string string number)


;Some tests to make sure that you define the question struct properly. 
(define q1 (make-question "What is Sirius' nickname when disguised as a dog?" "Padfoot" 10))

(check-expect (question? q1) #true)
(check-expect (check-response q1 "Spot") #false)
(check-expect
 ;; Right-click on with-output-to-string to view its documentation.
 ;; It runs the provided procedure and redirects the printed output to a string.
 (with-output-to-string
   (lambda () (show-text q1)))
 "Q: What is Sirius' nickname when disguised as a dog? (10 points)\n")


;Part 2
;Define the multichoice-question struct and its methods here. 
(define (multiplechoice-question question) (option-count options)
  #:methods
  (define (show-text q)
    (local[(define lst multiplechoice-question-options q)
           (define counter 1)]
    (begin
      (printf "Q: ~a (~a points)\nEnter a choice between 1 and ~a:\n" (question-text q) (question-points) (multiplechoice-question-option-count q))
      (while (not(empty? (lst)))
             (begin
               (printf "~a. ~a" 
                 
      
;a multiple choice question is a ...
; (make-multichoice-question string number number number (listof string))

(define q2
  (make-multichoice-question
   "Which spell does Hermoine use to repel Nagini as she attacks her and Harry in Bathilda Bagshot's house?"
   1  ;; answer
   10 ;; points
   3  ;; option-count
   (list "Confringo" "Bombarda Maxima" "Sectumsempra")))


(check-expect (multichoice-question? q2) #true)
(check-expect (multichoice-question-option-count q2) 3)
(check-expect
 ;; Right-click on with-output-to-string to view its documentation.
 ;; It runs the provided procedure and redirects the printed output to a string.
 (with-output-to-string
   (lambda () (show-text q2)))
 (string-append "Q: Which spell does Hermoine use to repel Nagini as she attacks"
                " her and Harry in Bathilda Bagshot's house? (10 points)\n"
                "Enter a number between 1 and 3:\n"
                "1. Confringo\n"
                "2. Bombarda Maxima\n"
                "3. Sectumsempra\n"))

;Define the numeric-question struct and its methods here. 

;a numeric question is a ...
; (make-numeric-question string number number number)

(define q3 (make-numeric-question
            "When Harry is appointed Seeker, how many years is it since someone his age has been appointed to a house Quidditch team?"
            100 ;; answer
            10  ;; points
            3)) ;; delta (the error range)

(check-expect (numeric-question? q3) #true)
(check-expect (check-response q3 101) #true)
(check-expect (check-response q3 109) #false)
(check-expect
 ;; Right-click on with-output-to-string to view its documentation.
 ;; It runs the provided procedure and redirects the printed output to a string.
 (with-output-to-string
   (lambda () (show-text q3)))
 (string-append "Q: When Harry is appointed Seeker, how many years is it since someone"
                " his age has been appointed to a house Quidditch team? (10 points)\n"))


;; runquiz: (listof question) -> void
;;   Takes a list of questions. In order, displays the question,
;;   gets a response from the user and checks the answer.
;; Effect: A quiz has been displayed and run.
(define (runquiz somequiz) 
  (local [(define user-response "")
          (define points-correct 0)
          (define total-points-possible 0)]
    (begin (printf "Welcome to my quiz!!\n\n")
           (for-each
            (lambda (q)
              (begin (show-text q)
                     (printf "> ")
                     (set! user-response (read-line))
                     (when (number? (question-answer/defaults-to-N/A q))
                       (set! user-response (string->number user-response)))
                     (cond
                       [(and (not (false? user-response))
                             (check-response q user-response))
                        (begin (printf "Yay!! Good job!\n\n")
                               (set! points-correct (+ points-correct
                                                       (question-points/defaults-to-0 q))))]
                       [else
                        (printf "Sorry - thats wrong!\n\n")])
                     (set! total-points-possible (+ total-points-possible
                                                    (question-points/defaults-to-0 q)))))
            somequiz)
           (printf "Your overall score is.... ~a out of ~a\n"
                   points-correct
                   total-points-possible))))

;; An example "quiz" (a list of questions)
(define myquiz (list q1 q2 q3)) 

;; Run the quiz on our list of questions
;;   Once you've completed parts 1 and 2, uncomment the runquiz line try to out the quiz! 
; (runquiz myquiz) ;; i.e. (runquiz (list q1 q2 q3))
