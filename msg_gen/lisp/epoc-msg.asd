
(cl:in-package :asdf)

(defsystem "epoc-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "Frecuencias" :depends-on ("_package_Frecuencias"))
    (:file "_package_Frecuencias" :depends-on ("_package"))
  ))