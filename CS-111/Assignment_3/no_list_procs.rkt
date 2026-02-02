#lang racket/base

(require (for-syntax racket/base)
         racket/stxparam
         (only-in lang/htdp-intermediate-lambda check-expect check-satisfied))

(provide
 (rename-out
  [marked-check-expect check-expect]
  [marked-check-satisfied check-satisfied]
  [marked-top-interaction #%top-interaction]
  [disallow-map map]
  [disallow-filter filter]
  [disallow-apply apply]
  [disallow-foldl foldl]
  [disallow-foldr foldr]
  [disallow-ormap ormap]
  [disallow-andmap andmap]))

(define-syntax-parameter allow? #f)

(define-for-syntax (make-marked-check-expr check-id)
  (λ (stx)
    (syntax-case stx ()
      [(form actual expected)
       (quasisyntax/loc stx
         (#,check-id actual
                     (syntax-parameterize ([allow? #t])
                       expected)))]
      [(form . rest)
       (quasisyntax/loc stx (#,check-id . rest))]
      [form
       (identifier? #'form)
       (quasisyntax/loc stx #,check-id)])))

(define-syntax marked-check-expect (make-marked-check-expr #'check-expect))
(define-syntax marked-check-satisfied (make-marked-check-expr #'check-satisfied))

(define-syntax (marked-top-interaction stx)
  (syntax-case stx ()
    [(form . expr)
     (syntax/loc stx
       (#%top-interaction . (syntax-parameterize ([allow? #t])
                              expr)))]))

(define-for-syntax (make-disallowed-id orig-id)
  (λ (stx)
    (cond
      [(syntax-parameter-value #'allow?)
       (syntax-case stx ()
         [(form . rest)
          (quasisyntax/loc stx (#,orig-id . rest))]
         [form
          (identifier? #'form)
          (quasisyntax/loc stx #,orig-id)])]
      [else
       (raise-syntax-error (syntax-e orig-id)
                           "this procedure can only be used in check-expect or check-satisfied"
                           stx)])))

(define-syntax (define-disallowed-id stx)
  (syntax-case stx ()
    [(form [new-id orig-id] ...)
     #'(begin
         (define-syntax new-id (make-disallowed-id #'orig-id))
         ...)]))

(define-disallowed-id
  [disallow-map map]
  [disallow-filter filter]
  [disallow-apply apply]
  [disallow-foldl foldl]
  [disallow-foldr foldr]
  [disallow-ormap ormap]
  [disallow-andmap andmap])
