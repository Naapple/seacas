if(CMAKE_PROJECT_NAME STREQUAL "SEACASProj")
TRIBITS_PACKAGE_DEFINE_DEPENDENCIES(
  LIB_OPTIONAL_PACKAGES SEACASExodus Zoltan
  LIB_OPTIONAL_TPLS HDF5 Pamgen CGNS ParMETIS Faodel Cereal DLlib Pthread ADIOS2 GTest Kokkos DataWarp fmt
)
else()
TRIBITS_PACKAGE_DEFINE_DEPENDENCIES(
  LIB_OPTIONAL_PACKAGES SEACASExodus Pamgen Zoltan Kokkos
  LIB_OPTIONAL_TPLS HDF5 CGNS ParMETIS Faodel Cereal DLlib Pthread DataWarp ADIOS2 GTest
)
endif()

TRIBITS_TPL_TENTATIVELY_ENABLE(DLlib)
