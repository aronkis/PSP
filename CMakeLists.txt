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
               mains/clientView.cc
               src/client.cc
               src/user.cc
               src/admin.cc
               src/connection.cc
               src/employee.cc
               src/room.cc
               src/hotel.cc
               gui/include/ClientGUI.h
               gui/ui/ClientUI/ClientGUI.ui
               gui/ClientGUI.cc)

add_executable(server_main 
              mains/server_main.cc
              src/server.cc)

add_executable(EmployeeGUI 
               mains/employeeView.cc
               src/client.cc
               src/user.cc
               src/admin.cc
               src/connection.cc
               src/employee.cc
               src/room.cc
               src/hotel.cc
               gui/include/EmployeeGUI.h
               gui/include/CreateRoomDialog.h
               gui/ui/EmployeeUI/EmployeeGUI.ui
               gui/ui/EmployeeUI/CreateRoomGUI.ui
               gui/CreateRoomDialog.cc
               gui/EmployeeGUI.cc)

target_compile_features(ClientGUI PUBLIC cxx_std_20)
target_compile_features(server_main PUBLIC cxx_std_20)
target_compile_features(EmployeeGUI PUBLIC cxx_std_20)

target_link_libraries(ClientGUI ${Boost_LIBRARIES})
target_link_libraries(server_main ${Boost_LIBRARIES})
target_link_libraries(EmployeeGUI ${Boost_LIBRARIES})
target_link_libraries(ClientGUI ${SQLite3_LIBRARIES})
target_link_libraries(server_main ${SQLite3_LIBRARIES})
target_link_libraries(EmployeeGUI ${SQLite3_LIBRARIES})
target_link_libraries(ClientGUI Qt5::Widgets)
target_link_libraries(EmployeeGUI Qt5::Widgets)

# qt5_add_resources(RESOURCES resources.qrc)
