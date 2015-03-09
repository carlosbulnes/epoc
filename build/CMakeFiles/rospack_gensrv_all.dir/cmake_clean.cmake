file(REMOVE_RECURSE
  "../msg_gen"
  "../srv_gen"
  "../src/epoc/msg"
  "../src/epoc/srv"
  "../msg_gen"
  "../srv_gen"
)

# Per-language clean rules from dependency scanning.
foreach(lang)
  include(CMakeFiles/rospack_gensrv_all.dir/cmake_clean_${lang}.cmake OPTIONAL)
endforeach()
