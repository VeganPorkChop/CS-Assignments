#lang htdp/asl

(require "quiz_lib.rkt")

;; a fun question is a ...
;; (make-fun-question string (listof string) (listof string))
;;   If a user answers with a particular choice, you can think of that as a vote
;;   for a particular outcome (the result of the quiz as a whole).
;; Note that corresponding-outcomes in each question could be ordered differently.
(define-struct fun-question [text choices corresponding-outcomes] 
  #:methods
  (define (show-text q)
    (local [(define (print-choices num-lbl choices)
              (when (not (empty? choices))
                (begin
                  (printf "  ~a. ~a\n" num-lbl (first choices))
                  (print-choices (+ num-lbl 1) (rest choices)))))]
      (begin
        (printf "Q: ~a\n" (fun-question-text q))
        (print-choices 1 (fun-question-choices q)))))
  
  ;; get-choice-from-number: fun-question number -> string
  ;;   Returns the choice associated with a particular number.
  (define (choice-ref q choice)
    ;; the list index starts at 0, so we need to subtract the choice 1
    (list-ref (fun-question-choices q) (- choice 1)))

  ;; get-corresponding-outcome-from-number: fun-question Number -> String
  ;;   Returns the outcome associated with a particular number.
  (define (corresponding-outcome-ref q choice)
    ;; the list index starts at 0, so we need to subtract the choice 1
    (list-ref (fun-question-corresponding-outcomes q) (- choice 1))))

;; Credit buzzfeed - https://www.buzzfeed.com/jenniferabidor/encanto-character-quiz 
(check-expect (choice-ref q1 5) "Shy")
(check-expect (corresponding-outcome-ref q1 5) "Bruno")
(define q1
  (make-fun-question
   "How would your friends describe you?"
   (list "Funny" "Strong" "Emotional" "Kind" "Shy" "Intense")
   (list "Dolores" "Luisa" "Pepa" "Mirabel" "Bruno" "Isabella")))

(check-expect (choice-ref q2 5) "No gift")
(check-expect (corresponding-outcome-ref q2 5) "Isabella")
(define q2
  (make-fun-question
   "Choose a gift you'd love to have."
   (list "Invisibility" "Mind Reading"
         "Ability to fly" "Knowing every language"
         "No gift" "Literally any gift")
   (list "Dolores" "Luisa" "Pepa" "Bruno" "Isabella" "Mirabel")))

(check-expect (choice-ref q3 5) "What Else Can I Do?")
(check-expect (corresponding-outcome-ref q3 5) "Pepa")
(define q3
  (make-fun-question
   "Pick the Encanto song you can't stop listening to."
   (list "The Family Madrigal"
         "Waiting on a Miracle"
         "Surface Pressure"
         "We Don't Talk About Bruno"
         "What Else Can I Do?"
         "Impossible to pick just one")
   (list "Dolores" "Mirabel" "Luisa" "Bruno" "Pepa" "Isabella")))

;; a quiz is a ...
;; (make-quiz string (listof fun-question) (listof string) (hash string number))
(define-struct quiz [title questions possible-outcomes scoring-of-outcomes]
  #:methods

  ;; reset-scoring-hash: quiz -> void
  ;;   For each outcome in possible-outcomes, sets the value associated it
  ;;   in the hash table in scoring-of-outcomes to 0.
  ;; Effect: scoring-of-outcomes attribute has changed, all values set to 0.
  (define (reset-scoring-hash q)
    (set-quiz-scoring-of-outcomes!
     q
     (make-hash
      (map (lambda (str) (list str 0))
           (quiz-possible-outcomes q)))))

  ;; update-scoring-hash: quiz string -> void
  ;;   Increments the scoring-of-outcomes hash, adding one to the value
  ;;   associated with the given outcome.
  ;; Effect: scoring-of-outcomes attribute has changed, incrementing value
  ;;  associated with the given by 1.
  (define (update-scoring-hash q str)
    (hash-set! (quiz-scoring-of-outcomes q)
               str
               (+ 1 (hash-ref (quiz-scoring-of-outcomes q) str))))

  ;; get-scoring-outcome: quiz -> String
  ;;   Iterates over the scoring-of-outcomes hash to find and return the
  ;;   outcome with the highest associated value.
  (define (get-scoring-outcome q)
    (local [(define (best-outcome outcomes best-so-far)
              (cond [(empty? outcomes) best-so-far]
                    [(> (hash-ref (quiz-scoring-of-outcomes q) (first outcomes))
                        (hash-ref (quiz-scoring-of-outcomes q) best-so-far))
                     (best-outcome (rest outcomes) (first outcomes))]
                    [else
                     (best-outcome (rest outcomes) best-so-far)]))]
      (best-outcome (rest (quiz-possible-outcomes q))
                    (first (quiz-possible-outcomes q))))))

;; an example "quiz" (a list of questions)
(define m1
  (make-fun-question
   "What do you do mid study sesh post sundown"
   (list "Snack run"
         "IG scrolling"
         "give up"
         "Microwaving leftovers and calling it cooking")
   (list "fat" "lazy" "lazy" "survivor")))

(define m2
  (make-fun-question
   "Pick a campus superpower."
   (list "Always finding an empty study room"
         "Laundry finishes exactly when I arrive"
         "Dining hall soda machine never breaks around you"
         "Professor grades homework you didnt do well on completion")
   (list "academic weapon" "lucky" "fat" "lucky")))

(define m3
  (make-fun-question
   "What do you tell youself in the mirror"
   (list "It'll probably be fine"
         "I need a little treat"
         "I gotta lock in"
         "I need to stop eating sugar")
   (list "academic weapon" "lazy" "survivor" "fat")))

(define encanto-quiz
  (make-quiz "Which Encanto character are you most like?"
             (list q1 q2 q3)
             (list "Dolores" "Luisa" "Pepa" "Mirabel" "Bruno" "Isabella")
             (make-hash)))

(define myquiz
  (make-quiz "What kind of college creature are you?"
             (list m1 m2 m3)
             (list "fat" "lazy" "academic weapon" "survivor" "lucky")
             (make-hash)))

;; A check-expect for reset-scoring-hash
(check-expect
 (local [(define testquiz
           (make-quiz "Title"
                      (list q1)
                      (list "Pepa" "Mirabel" "Bruno" "Isabella")
                      (make-hash)))]
   (begin
     (reset-scoring-hash testquiz)
     testquiz))
 (make-quiz "Title"
            (list q1)
            (list "Pepa" "Mirabel" "Bruno" "Isabella")
            (make-hash
             (list (list "Pepa" 0) (list "Mirabel" 0)
                   (list "Bruno" 0) (list "Isabella" 0)))))

;; A check-expect for update-scoring-hash
(check-expect
 (local [(define testquiz
           (make-quiz "Title"
                      (list q1)
                      (list "Pepa" "Mirabel" "Bruno" "Isabella")
                      (make-hash)))]
   (begin
     (reset-scoring-hash testquiz)
     (update-scoring-hash testquiz "Mirabel")
     (update-scoring-hash testquiz "Bruno")
     (update-scoring-hash testquiz "Bruno")
     (update-scoring-hash testquiz "Isabella")
     (quiz-scoring-of-outcomes testquiz)))
 (make-hash
  (list (list "Pepa" 0) (list "Mirabel" 1)
        (list "Bruno" 2) (list "Isabella" 1))))

;; A check-expect for get-scoring-outcome
(check-expect
 (local [(define testquiz
           (make-quiz "Title"
                      (list q1)
                      (list "Pepa" "Mirabel" "Bruno" "Isabella")
                      (make-hash)))]
   (begin
     (reset-scoring-hash testquiz)
     (update-scoring-hash testquiz "Mirabel")
     (update-scoring-hash testquiz "Bruno")
     (update-scoring-hash testquiz "Bruno")
     (update-scoring-hash testquiz "Isabella")
     (update-scoring-hash testquiz "Mirabel")
     (update-scoring-hash testquiz "Bruno")
     (get-scoring-outcome testquiz)))
 "Bruno")

;; runquiz: (listof question) -> void
;;   Takes a list of questions. In order, displays the question,
;;   gets a response from the user and checks the answer.
;; Effect: A quiz has been displayed and run.
(define (runquiz somequiz)
  (local [(define user-response "")
          (define user-responses (list))]
    (begin
      (printf "Welcome to my quiz!\n>>> ~a <<<\n" (quiz-title somequiz))
      (reset-scoring-hash somequiz)
      (for-each (lambda (q)
                  (begin (newline)
                         (show-text q)
                         (printf "> ")
                         (set! user-response (read))
                         (set! user-responses
                               (append user-responses
                                       (list (choice-ref q user-response))))
                         (update-scoring-hash somequiz
                                              (corresponding-outcome-ref q
                                                                         user-response))))
                (quiz-questions somequiz))
      (printf "\nYou answered...\n")
      (for-each (lambda (s) (printf "    - ~a\n" s)) user-responses)
      (printf "Your result is...\n~a\n"
              (get-scoring-outcome somequiz)))))

(runquiz myquiz)