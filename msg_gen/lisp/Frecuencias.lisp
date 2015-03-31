; Auto-generated. Do not edit!


(cl:in-package epoc-msg)


;//! \htmlinclude Frecuencias.msg.html

(cl:defclass <Frecuencias> (roslisp-msg-protocol:ros-message)
  ((datos
    :reader datos
    :initarg :datos
    :type (cl:vector cl:float)
   :initform (cl:make-array 14 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass Frecuencias (<Frecuencias>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Frecuencias>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Frecuencias)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name epoc-msg:<Frecuencias> is deprecated: use epoc-msg:Frecuencias instead.")))

(cl:ensure-generic-function 'datos-val :lambda-list '(m))
(cl:defmethod datos-val ((m <Frecuencias>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader epoc-msg:datos-val is deprecated.  Use epoc-msg:datos instead.")
  (datos m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Frecuencias>) ostream)
  "Serializes a message object of type '<Frecuencias>"
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'datos))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Frecuencias>) istream)
  "Deserializes a message object of type '<Frecuencias>"
  (cl:setf (cl:slot-value msg 'datos) (cl:make-array 14))
  (cl:let ((vals (cl:slot-value msg 'datos)))
    (cl:dotimes (i 14)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-double-float-bits bits)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Frecuencias>)))
  "Returns string type for a message object of type '<Frecuencias>"
  "epoc/Frecuencias")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Frecuencias)))
  "Returns string type for a message object of type 'Frecuencias"
  "epoc/Frecuencias")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Frecuencias>)))
  "Returns md5sum for a message object of type '<Frecuencias>"
  "3cc745c08934b0cd21fbac2bdbf11b12")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Frecuencias)))
  "Returns md5sum for a message object of type 'Frecuencias"
  "3cc745c08934b0cd21fbac2bdbf11b12")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Frecuencias>)))
  "Returns full string definition for message of type '<Frecuencias>"
  (cl:format cl:nil "float64[14] datos~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Frecuencias)))
  "Returns full string definition for message of type 'Frecuencias"
  (cl:format cl:nil "float64[14] datos~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Frecuencias>))
  (cl:+ 0
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'datos) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Frecuencias>))
  "Converts a ROS message object to a list"
  (cl:list 'Frecuencias
    (cl:cons ':datos (datos msg))
))
