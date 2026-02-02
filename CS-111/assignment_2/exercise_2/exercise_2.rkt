#lang htdp/isl+

(require "remove_duplicates.rkt")

;; DON'T CHANGE EXISTING check-expectS!!!
;; These are just tests to make sure all of your images are named correctly for grading
(check-satisfied recording-procedure-count number?)
(check-satisfied tango-song
                 (lambda (unused)
                   #true))
(check-satisfied is-a-record? procedure?)
(check-satisfied a-selector procedure?)
(check-satisfied another-selector procedure?)
(check-satisfied count-record procedure?)
(check-satisfied two-genres procedure?)
(check-satisfied classic-lib list?)
(check-satisfied rock-lib list?)
(check-satisfied display-record
                 (lambda (unused)
                   #true))
(check-satisfied contains-the?
                 (lambda (unused)
                   #true))
(check-satisfied library-genres procedure?)
(check-satisfied genre-recordings procedure?)
(check-satisfied categorize-by-genre procedure?)
(check-satisfied artists-count-by-genre procedure?)




;; This defines the basic recording datatype.
(define-struct recording [title genre artist])
;; A Recording is a structure: (make-recording String String String)
;; - `title' stores the title of a recording
;; - `genre' classifies the its genre
;; - `artist' stores the name of the composer or the singer


;; Two example Recording data objects
(define example-song (make-recording "Blowin' In The Wind" "folk" "Bob Dylan"))
(define another-song (make-recording "The Sound of Silence" "folk" "Simon & Garfunkel"))


;; access-example-song : (recording -> string) -> string
;;   A procedure that accesses the fields of `example-song'
;;   according to the given `selector'
(define access-example-song
  (lambda (selector)
    (selector example-song)))


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 3.1. Getting familiar with recording data objects
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; Write your solution for Problem 3.1 here
(define recording-procedure-count 5)
;;could also be 8, not quite sure because the args to the struct are mutable and i forgot if we learned that and if it counts

(define tango-song
  (make-recording "Por una Cabeza" "tango" "Carlos Gardel"))

(define (is-a-record? obj)
  (if (recording? obj) #true #false))

(check-expect (is-a-record? tango-song) #true)


(define (a-selector obj)
  (recording-artist obj))

(check-expect (access-example-song a-selector) "Bob Dylan")

(define (another-selector obj)
  (recording-title obj))

(check-expect (access-example-song another-selector) "Blowin' In The Wind")


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 3.2. Counting recordings
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; Write your solution for Problem 3.2, count-record, here

;; count-record : any any any -> number
;;   Count the number of recording data objects in the inputs.

(define (count-record rec1 rec2 rec3)
  (local[(define helper (lambda (rec acc)
                 (if (is-a-record? rec) (+ 1 acc) acc)))]
  (helper rec3 (helper rec2 (helper rec1 0)))))
  
(check-expect (count-record tango-song example-song make-recording) 2)
(check-expect (count-record #true 5 "Bob Dylan") 0)
  



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 3.3. Comparing genres
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define pop-song (make-recording "Stronger" "pop" "Kelly Clarkson"))

;; Write your solution for Problem 3.3, two-genres, here
(define two-genres (lambda (rec1 rec2 rec3)
                     (cond [(string=? (recording-genre rec1) (recording-genre rec2)) #true]
                           [(string=? (recording-genre rec2) (recording-genre rec3)) #true]
                           [(string=? (recording-genre rec1) (recording-genre rec3)) #true]
                           [else #false]
                           )))


;; two-genres : recording recording recording -> boolean
;;   Outputs #true if at least two out of the three inputs have the same genre.
(check-expect (two-genres example-song tango-song pop-song) #false)
(check-expect (two-genres example-song example-song example-song) #true)



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 4.1. Music libraries
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define folk-lib (list example-song another-song))

(define pop-lib
  (list (make-recording "Stronger" "pop" "Kelly Clarkson")))

;; Write your solution for Problem 4.1, rock-lib and classic-lib, here
(define classic-lib
  (list (make-recording "Fur Elise" "classic" "Mozart")))

(define rock-lib
  (list (make-recording "Smells Like Teen Spirit" "rock" "Nirvana")(make-recording "Bohemian Rhapsody" "rock" "Queen")(make-recording "Something In The Way" "rock" "Nirvana")))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 4.2. `map`: transforming a library as a whole
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(check-expect (map display-record pop-lib) (list "Kelly Clarkson, Stronger"))
(check-expect (map display-record folk-lib)
              (list "Bob Dylan, Blowin' In The Wind"
                    "Simon & Garfunkel, The Sound of Silence"))

;; Write your solution for Problem 4.2, display-record, here

(define display-record (lambda (record)
                         (string-append (recording-artist record) ", " (recording-title record))))

(check-expect (map display-record pop-lib) (list "Kelly Clarkson, Stronger"))
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 4.3. `filter`: searching for specific elements in a library
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(check-expect (filter contains-the? folk-lib) folk-lib)

;; Write your solution for Problem 4.3, contains-the?, here

(define contains-the? (lambda(record)
                        (string-contains? "The" (recording-title record))))

(check-expect (contains-the? example-song) #true)


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 4.4. Summarizing the genres in a library
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; Write your solution for Problem 4.4, library-genres, here
(define library-genres (lambda(lst)
                         (remove-duplicates(map recording-genre lst))))

(check-expect (library-genres (append pop-lib classic-lib)) (list "pop" "classic"))

;; library-genres : (listof recording) -> (listof string)
;;   Takes a music library and summarizes the genres of recordings in the library

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 4.5. Searching for recordings by genre
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; Write your solution for Problem 4.5, genre-recordings, here
(define (genre-recordings g lib)
  (cond
    [(empty? lib) empty]
    [(string=? g (recording-genre (first lib)))
     (cons (first lib)
           (genre-recordings g (rest lib)))]
    [else
     (genre-recordings g (rest lib))]))
                           

(check-expect (genre-recordings "pop" (append folk-lib pop-lib rock-lib)) (genre-recordings "pop" pop-lib))
;; genre-recordings : string (listof recording) -> (listof recording)
;;   Takes a genre, a music library and outputs the list of all recordings
;;   that are of the same, given genre in the library

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 4.6. Categorizing the libraries by genres
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; Write your solution for Problem 4.6, categorize-by-genre, here

;; categorize-by-genre : (listof recording) -> (listof (listof recording))
(define (categorize-by-genre-helper genres lib)
  (cond
    [(empty? genres) empty]
    [else
     (cons (genre-recordings (first genres) lib)
           (categorize-by-genre-helper (rest genres) lib))]))

(define (categorize-by-genre lib)
  (cond
    [(empty? (library-genres lib)) empty]
    [else
     (cons (genre-recordings (first (library-genres lib)) lib)
           (categorize-by-genre-helper (rest (library-genres lib)) lib))]))
                              

(check-expect
 (categorize-by-genre (append folk-lib pop-lib))
 (list folk-lib pop-lib))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 4.7. Counting artists by genres
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; Write your solution for Problem 4.7, artists-count-by-genre, here
;; artists-count-by-genre : (listof recording) -> (listof (list string number))
(define (artists-count-by-genre lib)
  (local [(define categorized (categorize-by-genre lib))
          (define (artists-in sublib)
            (map recording-artist sublib))
          (define (artist-count sublib)
            (length (remove-duplicates (artists-in sublib))))
          (define (genre-of sublib)
            (recording-genre (first sublib)))
          (define (one-result sublib)
            (list (genre-of sublib) (artist-count sublib)))]
    (map one-result categorized)))


;; artists-count-by-genre : (listof recording) -> (listof (list string number))
(check-expect
 (artists-count-by-genre (append folk-lib pop-lib))
 (list (list "folk" 2)
       (list "pop" 1)))

