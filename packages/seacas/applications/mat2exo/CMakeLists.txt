
IF (TPL_ENABLE_Matio)
TRIBITS_SUBPACKAGE(Mat2exo)

LINK_DIRECTORIES(${Matio_LIBRARY_DIRS})
TRIBITS_INCLUDE_DIRECTORIES(
  "${Matio_INCLUDE_DIRS}"
  "${CMAKE_CURRENT_SOURCE_DIR}"
)

SET(CODE mat2exo)
SET(HEADERS "")

TRIBITS_ADD_EXECUTABLE(
  ${CODE}
  NOEXEPREFIX
  NOEXESUFFIX
  SOURCES mat2exo.C
  COMM serial mpi
  INSTALLABLE
  )

TRIBITS_SUBPACKAGE_POSTPROCESS()
ENDIF()
