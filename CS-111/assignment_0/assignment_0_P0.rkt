#lang htdp/isl+

;; DON'T CHANGE THESE!!!
;; These are just tests to make sure all of your images are named correctly for grading
(check-expect (image? solid-circle) #t)
(check-expect (image? solid-square) #t)
(check-expect (image? outline-circle) #t)
(check-expect (image? outline-square) #t)
(check-expect (image? row-of-circles) #t)
(check-expect (image? column-of-circles) #t)
(check-expect (image? nested-squares) #t)
(check-expect (image? rotated-squares) #t)
(check-expect (image? flag-of-chicago) #t)




(require 2htdp/image)

; Write your code here!
(define colors "purple" )
  
(define solid-circle(circle 50 "solid" colors))

(define solid-square(square 100 "solid" "grey"))

(define outline-circle(circle 50 "outline" "red"))

(define outline-square(square 100 "outline" "blue"))

(define row-of-circles(beside (circle 50 "solid" "red") (circle 50 "solid" "blue")(circle 50 "solid" "green")))

(define column-of-circles(above (circle 50 "solid" "red") (circle 50 "solid" "blue")(circle 50 "solid" "green")))
;for overlay the first input it the one on top, underlay: the first input is the one on bottom;
(define nested-squares (underlay (square 80 "solid" "red")
                                (square 60 "solid" "blue")
                                (square 40 "solid" "green")
                                (square 20 "solid" "black")))

(define rotated-squares(rotate 45
                        (underlay (square 80 "solid" "red")
                                (square 60 "solid" "blue")
                                (square 40 "solid" "green")
                                (square 20 "solid" "black"))))

(define chicago-star(radial-star 6 8 20 "solid" "red"))

(define flag-of-chicago(underlay/offset
                        (underlay/align "center" "center"
                                       (rectangle 180 120 "outline" "black")
                                       ;the four stars 
                                       (underlay/offset chicago-star
                                                        -90 0
                                                        (underlay/offset chicago-star
                                                                         0 0
                                                                         (underlay/offset chicago-star
                                                                                          90 0
                                                                                          chicago-star))))
                        ;these are the flags blue bars
                                       0 0
                                       (underlay/offset(rectangle 180 20 "solid" "lightblue")
                                                        0 65
                                                        (rectangle 180 20 "solid" "lightblue"))))
                                                        


                                        

  
