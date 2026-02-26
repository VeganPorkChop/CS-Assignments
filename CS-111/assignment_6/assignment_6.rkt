#lang htdp/asl

(require "./file_operations.rkt")

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Part 1: Recursion over the File System Structure
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; tip: the list procedures: map, filter, apply, etc, will be handy in this assignment!
;; check-expect's are not absolutely necessary for this assignment. You can
;; run each procedure in the REPL (bottom window) and observe the output to see
;; if they're correct. See the PDF for more details:)

;; sum : (listof number) -> number

(define (sum lst)
  (if (empty? lst) 0 (+ (first lst) (sum (rest lst)))))

(check-satisfied sum procedure?)

;; count-files : path -> number
(define (count-files dir-path)
  (+ (length (directory-files dir-path))
  (sum (map count-files (directory-subdirectories dir-path)))))

(check-satisfied count-files procedure?)

;; directory-size : path -> number
(define (directory-size dir-path)
  (+ (sum (map file-size (directory-files dir-path)))
     (sum (map directory-size (directory-subdirectories dir-path)))))
          
(check-satisfied directory-size procedure?)

;; concat : (listof (listof path)) -> (listof path)
(define (concat lst-of-lists)
  (apply append lst-of-lists))

(check-satisfied concat procedure?)
(check-expect
 (concat
  (list (list (build-path "test"))
        (list (build-path "test" "test_2")
              (build-path "test" "test_3"))))
 (list (build-path "test")
       (build-path "test" "test_2")
       (build-path "test" "test_3")))

;; all-directories : path -> (listof path)
(define (all-directories dir-path)
  (append (directory-files dir-path) (map all-directories (directory-subdirectories dir-path))))

(check-satisfied all-directories procedure?)

;; search-file-name : string path -> (listof path)
(define (search-file-name name dir-path)
  (append
   (filter (lambda (p)
             (string=? name
                       (substring (path->string (path-filename p))
                                  0 (- (string-length (path->string (path-filename p))) 4))))
           (directory-files dir-path))
   (concat (map (lambda (d) (search-file-name name d))
                (directory-subdirectories dir-path)))))

(check-satisfied search-file-name procedure?)
(check-expect
 (search-file-name "test" (string->path "test"))
 (list (build-path "test" "test.txt")))
(check-expect
 (search-file-name "bar" (string->path "test"))
 (list (build-path "test" "test_2" "bar.txt")))




;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Part 2: Imperative Programming and File Operations
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

; backup! : Path Path -> Void
;
; Recursively copies all the files and subdirectories in the `from`
; directory to the `to` directory. This is a modified version of the
; `copy-tree` procedure we discussed in class.
;
; EFFECT: `to` and all its contents now exist
; EFFECT: may overwrite existing files at `to`
(define (backup! from to) 
  (begin
    ; create the destination directory if it doesn't already exist
    (unless (directory-exists? to)
      (make-directory! to))

    ; for each file (leaf node) in the origin directory,
    ; copy it over to the destination directory
    (for-each (λ (file)
                ; print the name of the file being copied into the REPL
                ; for more on how `printf` works, see Appendix 1 in the pdf
                ;when file doesnt exist in to directory or its "out of date"
                (when (or (not(file-exists? (build-path to (path-filename file)))) (not(equal? (file-or-directory-modify-seconds file) (file-or-directory-modify-seconds (build-path to (path-filename file))))))
                  (begin
                    (printf "Copying file ~A to ~A~n"
                            file
                            (build-path to (path-filename file)))
                    (copy-file! file
                                (build-path to (path-filename file))
                                #true))))
                  (directory-files from))

    ; for each folder (recursive child node) in the origin directory,
    ; recursively `backup!` its contents
    (for-each (λ (subdir)
                (backup! subdir
                         ; add the subdirectory's name to the
                         ; end of the original destination path
                         (build-path to (path-filename subdir))))
              (directory-subdirectories from))))
