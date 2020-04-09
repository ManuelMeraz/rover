# Add all targets to the build-tree export set
export(TARGETS motor_controls FILE "${PROJECT_BINARY_DIR}/gpio-bridge-targets.cmake")

# Export the package for use from the build-tree
# (this registers the build-tree with a global CMake-registry)
export(PACKAGE gpio_bridge)

# Create the gpio-bridge-config.cmake and gpio-bridge-config-version.cmake files
file(RELATIVE_PATH REL_INCLUDE_DIR "${INSTALL_CMAKE_DIR}" "${INSTALL_INCLUDE_DIR}")
# ... for the build tree
set(CONF_INCLUDE_DIRS "${PROJECT_SOURCE_DIR}" "${PROJECT_BINARY_DIR}")
configure_file(cmake/gpio-bridge-config.cmake.in "${PROJECT_BINARY_DIR}/gpio-bridge-config.cmake" @ONLY)
# ... for the install tree
set(CONF_INCLUDE_DIRS "\${GPIO_BRIDGE_CMAKE_DIR}/${REL_INCLUDE_DIR}")
configure_file(cmake/gpio-bridge-config.cmake.in "${PROJECT_BINARY_DIR}/${CMAKE_FILES_DIRECTORY}/gpio-bridge-config.cmake" @ONLY)
# ... for both
configure_file(cmake/gpio-bridge-config-version.cmake.in "${PROJECT_BINARY_DIR}/gpio-bridge-config-version.cmake" @ONLY)

# Install the gpio-bridge-config.cmake and gpio-bridge-config-version.cmake
install(FILES
        "${PROJECT_BINARY_DIR}/${CMAKE_FILES_DIRECTORY}/gpio-bridge-config.cmake"
        "${PROJECT_BINARY_DIR}/gpio-bridge-config-version.cmake"
        DESTINATION
        "${INSTALL_CMAKE_DIR}" COMPONENT dev)

install(DIRECTORY include/ DESTINATION ${INSTALL_INCLUDE_DIR})

# Install the export set for use with the install-tree
install(EXPORT gpio-bridge-targets
        DESTINATION "${INSTALL_CMAKE_DIR}"
        COMPONENT dev)