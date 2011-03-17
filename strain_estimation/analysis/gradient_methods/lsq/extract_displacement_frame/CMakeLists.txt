cmake_minimum_required(VERSION 2.8)
cmake_policy(VERSION 2.8)

project( edf )

find_package( ITK REQUIRED )
include( ${ITK_USE_FILE} )

add_executable( extract-displacement-frame
  extract_displacement_frame.cxx
  )
target_link_libraries( extract-displacement-frame
  ITKCommon
  ITKIO
  )
