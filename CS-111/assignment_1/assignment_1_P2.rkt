#lang htdp/isl+

(require 2htdp/image)
(require "./iterated_images.rkt")

;; DON'T CHANGE EXISTING check-expectS!!!
;; These are just tests to make sure all of your images are named correctly for grading
(check-satisfied question-3.1 image?)
(check-satisfied question-3.2 image?)
(check-satisfied question-3.3 image?)
(check-satisfied question-3.4 image?)
(check-satisfied test-4.1.1 image?)
(check-satisfied triangle-row procedure?)
(check-satisfied test-4.2.1 image?)
(check-satisfied colorful-triangle-row procedure?)
(check-satisfied test-4.3.1 image?)
(check-satisfied colorful-triangle-grid procedure?)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Part I: Iterated Expressions
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Question 3.1
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(check-expect question-3.1
              .)

;; Write your solution for question-3.1 here using beside
(define question-3.1
  (beside
   (triangle 30 "outline" "violet")
   (triangle 60 "outline" "violet")
   (triangle 90 "outline" "violet")
   (triangle 120 "outline" "violet")))





;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Question 3.2
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(check-expect question-3.2
              .)

;; Write your solution for question-3.2 here using iterated-beside
(define question-3.2
  (iterated-beside(lambda(n)
                    (triangle (* (+ n 1) 30) "outline" "violet"))
                  4))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Question 3.3: A Simple Flower
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(check-expect question-3.3
              .)

;; Define question-3.3 here
(define question-3.3
  (iterated-overlay
   (lambda(n)
     (rotate (* n 36) (ellipse 120 30 "solid" "orange")))
   5))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Question 3.4: A Colorful Flower
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(check-expect question-3.4
              .)

;; Define question-3.4 here
(define question-3.4
  (iterated-overlay
   (lambda(n)
     (rotate (* 36 n) (ellipse 120 30 "solid" (interpolate-colors "orange" "brown" (/ n 4))))
     )5))
                               

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Part II: Function Abstractions
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Question 4.1.1--2: A Row of Triangles, Revisited
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; The example image of 4.1.1
(check-expect test-4.1.1
              .)

;; Write your solution for 4.1.1 here using beside
(define test-4.1.1
  (beside
   (triangle 50 "outline" "red")
   (triangle 100 "outline" "red")
   (triangle 150 "outline" "red")
   ))

;; The (example) tests of 4.1.2
(check-expect (triangle-row 4 120 "violet")
              question-3.1)
(check-expect (triangle-row 3 150 "red")
              test-4.1.1)
;; Write your solution for 4.1.2 here

;; triangle-row : number number color -> image
;; Purpose: the triangle-row procedure takes three inputs and returns
;;   a row of triangles. The inputs specify the number of triangles, the size
;;   of the largest triangle, and the color of the triangles.
(define triangle-row
  (lambda (num-triangles side-len the-color)
    (iterated-beside (lambda (n)
     (triangle ( / (* (+ n 1) side-len) num-triangles) "outline" the-color))num-triangles)))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Question 4.2: Colorful Triangles
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; The example image of 4.2.1
(check-expect test-4.2.1
              .)

;; Write your solution for 4.2.1 here using beside
(define test-4.2.1
  (beside (triangle 40 "outline" "red")
          (triangle 80 "outline" "blue")))

;; You must turn the images test-4.2.1 and example-4.2.2 into test cases.
(define example-4.2.2
  .)
(check-expect (colorful-triangle-row 2 80 "red" "blue")
 test-4.2.1)
(check-expect (colorful-triangle-row 3 90 "red" "blue")
 example-4.2.2)



;; Write your solution for 4.2.2, the colorful-triangle-row function, here

;; colorful-triangle-row : number number color color -> image
;; Purpose: The question-4.2.2 procedure takes four inputs and returns
;;   a row of triangles. The inputs specify the number of triangles, the size
;;   of the largest triangle, and the color of the leftmost and rightmost triangles.

(define colorful-triangle-row
  (lambda(tri len c1 c2)
    (iterated-beside(lambda(n)
                      (triangle (* len (/ (+ n 1) tri)) "outline" (interpolate-colors c1 c2 (/ n (- tri 1)))))
                    tri)))


;; An example expression that produces the same image as example-4.2.2 using `color`. 
(check-expect example-4.2.2
              (beside (triangle 30 "outline" "red")
                      (triangle 60 "outline" (make-color 128 0 128))
                      (triangle 90 "outline" "blue")))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Question 4.3: Colorful Triangles
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; The example image of 4.3.1
(check-expect test-4.3.1
              .)

;; Write your solution for 4.3.1 here using above and beside
(define test-4.3.1
  (above
   (beside
    (triangle 40 "outline" "red")
    (triangle 80 "outline" "orange")
    )
   (beside
    (triangle 40 "outline" "purple")
    (triangle 80 "outline" "blue")
   )
   )
  )

;; You must turn the images test-4.3.1 and example-4.3.2 into test cases.
(define example-4.3.2
  .)
(check-expect (colorful-triangle-grid 2 2 80 "red" "purple" "orange" "blue")
 test-4.3.1)
(check-expect (colorful-triangle-grid 3 5 50 "green" "black" "black" "green")
 example-4.3.2)

;; Write your solution for 4.3.2, the colorful-triangle-grid function, here
(define colorful-triangle-grid
  (lambda (num-rows num-cols side-len tl bl tr br)
    (iterated-above
     (lambda (r)
       (colorful-triangle-row
        num-cols
        side-len
        (interpolate-colors tl bl (/ r (- num-rows 1)))
        (interpolate-colors tr br (/ r (- num-rows 1)))))
     num-rows)))


;; colorful-triangle-grid : integer integer integer color color color color --> image
;; Purpose: The question-4.2.2 procedure takes seven inputs and returns
;;   a grid of triangles. The inputs specify the number of triangles vertically and horizontally, the size
;;   of the largest and rightmost triangles, and the color of the upper leftmost, lower leftmost, upper rightmost and lower rightmost triangles.
;; AS A NOTE: DISREGARD THE VARIABLE NAMES!!!! THEYRE MISNAMED AND CAUSE GREAT CONFUSION WHEN LOOKING CLOSELY!!!