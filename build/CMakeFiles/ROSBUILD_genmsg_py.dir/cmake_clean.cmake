FILE(REMOVE_RECURSE
  "../msg_gen"
  "../src/epoc/msg"
  "../msg_gen"
  "CMakeFiles/ROSBUILD_genmsg_py"
  "../src/epoc/msg/__init__.py"
  "../src/epoc/msg/_Frecuencias.py"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
