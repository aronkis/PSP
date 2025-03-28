CMAKE_MINIMUM_REQUIRED(VERSION 3.31)
project(ClientServer)

cmake_policy(SET CMP0167 NEW)
set(CMAKE_CXX_STANDARD 20)

find_package(Boost REQUIRED COMPONENTS serialization)
find_package(Qt6 REQUIRED COMPONENTS Widgets)
find_package(SQLite3 REQUIRED)

include_directories(${Boost_INCLUDE_DIRS})
include_directories(${SQLite3_INCLUDE_DIRS})
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)

add_executable(ClientPresenter 
               mains/clientPresenter.cc
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

add_executable(EmployeePresenter
               mains/employeePresenter.cc
               src/client.cc
               src/user.cc
               src/admin.cc
               src/connection.cc
               src/employee.cc
               src/room.cc
               src/hotel.cc
               gui/include/EmployeeGUI.h
               gui/include/LogInDialog.h
               gui/include/CreateRoomDialog.h
               gui/include/ReadRoomDialog.h
               gui/include/UpdateRoomDialog.h
               gui/include/DeleteRoomDialog.h
               gui/ui/EmployeeUI/EmployeeGUI.ui
               gui/ui/EmployeeUI/LogInGUI.ui
               gui/ui/EmployeeUI/CreateRoomGUI.ui
               gui/ui/EmployeeUI/ReadRoomGUI.ui
               gui/ui/EmployeeUI/UpdateRoomGUI.ui
               gui/ui/EmployeeUI/DeleteRoomGUI.ui
               gui/LogInDialog.cc
               gui/CreateRoomDialog.cc
               gui/ReadRoomDialog.cc
               gui/UpdateRoomDialog.cc
               gui/DeleteRoomDialog.cc
               gui/EmployeeGUI.cc)

target_compile_features(ClientPresenter PUBLIC cxx_std_20)
target_compile_features(server_main PUBLIC cxx_std_20)
target_compile_features(EmployeePresenter PUBLIC cxx_std_20)

target_link_libraries(ClientPresenter ${Boost_LIBRARIES})
target_link_libraries(server_main ${Boost_LIBRARIES})
target_link_libraries(EmployeePresenter ${Boost_LIBRARIES})
target_link_libraries(ClientPresenter ${SQLite3_LIBRARIES})
target_link_libraries(server_main ${SQLite3_LIBRARIES})
target_link_libraries(EmployeePresenter ${SQLite3_LIBRARIES})
target_link_libraries(ClientPresenter Qt6::Widgets)
target_link_libraries(EmployeePresenter Qt6::Widgets)

# qt5_add_resources(RESOURCES resources.qrc)
