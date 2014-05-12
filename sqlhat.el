(pymacs-load "sqlhat")

(defun sqlhat-connect-mysql ()
;  (interactive "p")
;  (sqlhat-init (buffer-string))
  (setq sqlhat-connection-information
	'(pool-a
	  (sql-product 'mysql)
	  (sql-server (sqlhat-getParameter "hostname"))
	  (sql-user (sqlhat-getParameter "user"))
	  (sql-password (sqlhat-getParameter "password"))
	  (sql-database (sqlhat-getParameter "wftest"))
	  )
	)
  (eval `(let ,(cdr sqlhat-connection-information)
	   (flet ((sql-get-login (&rest what)))
	     (sql-product-interactive sql-product)))))



(defun sqlhat-connect (name)
  ""
  (interactive "p")
  (sqlhat-init (buffer-string))
  (setq product (sqlhat-getParameter "product"))
  (if (string-equal "mysql" product)
      (sqlhat-connect-mysql)
    (message "Only support MySQL now")
    )
  )
 

(provide 'sqlhat)
