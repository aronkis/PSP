CMAKE_MINIMUM_REQUIRED(VERSION 3.31)
project(ClientServer)

cmake_policy(SET CMP0167 NEW)
set(CMAKE_CXX_STANDARD 20)

find_package(Boost REQUIRED COMPONENTS serialization)
find_package(Qt5 REQUIRED COMPONENTS Widgets)
find_package(SQLite3 REQUIRED)

include_directories(${Boost_INCLUDE_DIRS})
include_directories(${SQLite3_INCLUDE_DIRS})
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)

add_executable(ClientGUI 
               mains/client_main.cc
               src/client.cc
               src/user.cc
               src/admin.cc
               src/connection.cc
               src/employee.cc
               src/room.cc
               src/hotel.cc
               gui/include/ClientGUI.h
               gui/ui/ClientGUI.ui
               gui/ClientGUI.cc)

add_executable(server_main 
              mains/server_main.cc
              src/server.cc)

add_executable(employee_main 
               mains/employee_main.cc
               src/client.cc
               src/user.cc
               src/admin.cc
               src/connection.cc
               src/employee.cc
               src/room.cc
               src/hotel.cc)

target_compile_features(ClientGUI PUBLIC cxx_std_20)
target_compile_features(server_main PUBLIC cxx_std_20)
target_compile_features(employee_main PUBLIC cxx_std_20)

target_link_libraries(ClientGUI ${Boost_LIBRARIES})
target_link_libraries(server_main ${Boost_LIBRARIES})
target_link_libraries(employee_main ${Boost_LIBRARIES})
target_link_libraries(ClientGUI ${SQLite3_LIBRARIES})
target_link_libraries(server_main ${SQLite3_LIBRARIES})
target_link_libraries(employee_main ${SQLite3_LIBRARIES})
target_link_libraries(ClientGUI Qt5::Widgets)
target_link_libraries(employee_main Qt5::Widgets)

# qt5_add_resources(RESOURCES resources.qrc)
