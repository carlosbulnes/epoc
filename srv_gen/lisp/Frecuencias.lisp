; Auto-generated. Do not edit!


(cl:in-package epoc-srv)


;//! \htmlinclude Frecuencias-request.msg.html

(cl:defclass <Frecuencias-request> (roslisp-msg-protocol:ros-message)
  ((sen
    :reader sen
    :initarg :sen
    :type (cl:vector cl:float)
   :initform (cl:make-array 14 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass Frecuencias-request (<Frecuencias-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Frecuencias-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Frecuencias-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name epoc-srv:<Frecuencias-request> is deprecated: use epoc-srv:Frecuencias-request instead.")))

(cl:ensure-generic-function 'sen-val :lambda-list '(m))
(cl:defmethod sen-val ((m <Frecuencias-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader epoc-srv:sen-val is deprecated.  Use epoc-srv:sen instead.")
  (sen m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Frecuencias-request>) ostream)
  "Serializes a message object of type '<Frecuencias-request>"
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'sen))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Frecuencias-request>) istream)
  "Deserializes a message object of type '<Frecuencias-request>"
  (cl:setf (cl:slot-value msg 'sen) (cl:make-array 14))
  (cl:let ((vals (cl:slot-value msg 'sen)))
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Frecuencias-request>)))
  "Returns string type for a service object of type '<Frecuencias-request>"
  "epoc/FrecuenciasRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Frecuencias-request)))
  "Returns string type for a service object of type 'Frecuencias-request"
  "epoc/FrecuenciasRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Frecuencias-request>)))
  "Returns md5sum for a message object of type '<Frecuencias-request>"
  "c12060a30a7682910d5c890d5372e100")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Frecuencias-request)))
  "Returns md5sum for a message object of type 'Frecuencias-request"
  "c12060a30a7682910d5c890d5372e100")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Frecuencias-request>)))
  "Returns full string definition for message of type '<Frecuencias-request>"
  (cl:format cl:nil "float64[14] sen~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Frecuencias-request)))
  "Returns full string definition for message of type 'Frecuencias-request"
  (cl:format cl:nil "float64[14] sen~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Frecuencias-request>))
  (cl:+ 0
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'sen) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Frecuencias-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Frecuencias-request
    (cl:cons ':sen (sen msg))
))
;//! \htmlinclude Frecuencias-response.msg.html

(cl:defclass <Frecuencias-response> (roslisp-msg-protocol:ros-message)
  ((a
    :reader a
    :initarg :a
    :type cl:float
    :initform 0.0))
)

(cl:defclass Frecuencias-response (<Frecuencias-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Frecuencias-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Frecuencias-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name epoc-srv:<Frecuencias-response> is deprecated: use epoc-srv:Frecuencias-response instead.")))

(cl:ensure-generic-function 'a-val :lambda-list '(m))
(cl:defmethod a-val ((m <Frecuencias-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader epoc-srv:a-val is deprecated.  Use epoc-srv:a instead.")
  (a m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Frecuencias-response>) ostream)
  "Serializes a message object of type '<Frecuencias-response>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'a))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Frecuencias-response>) istream)
  "Deserializes a message object of type '<Frecuencias-response>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'a) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Frecuencias-response>)))
  "Returns string type for a service object of type '<Frecuencias-response>"
  "epoc/FrecuenciasResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Frecuencias-response)))
  "Returns string type for a service object of type 'Frecuencias-response"
  "epoc/FrecuenciasResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Frecuencias-response>)))
  "Returns md5sum for a message object of type '<Frecuencias-response>"
  "c12060a30a7682910d5c890d5372e100")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Frecuencias-response)))
  "Returns md5sum for a message object of type 'Frecuencias-response"
  "c12060a30a7682910d5c890d5372e100")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Frecuencias-response>)))
  "Returns full string definition for message of type '<Frecuencias-response>"
  (cl:format cl:nil "float64 a~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Frecuencias-response)))
  "Returns full string definition for message of type 'Frecuencias-response"
  (cl:format cl:nil "float64 a~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Frecuencias-response>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Frecuencias-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Frecuencias-response
    (cl:cons ':a (a msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Frecuencias)))
  'Frecuencias-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Frecuencias)))
  'Frecuencias-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Frecuencias)))
  "Returns string type for a service object of type '<Frecuencias>"
  "epoc/Frecuencias")