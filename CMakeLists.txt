CMAKE_MINIMUM_REQUIRED(VERSION 3.10)
project(ClientServer)

cmake_policy(SET CMP0167 NEW)
set(CMAKE_CXX_STANDARD 20)
find_package(Boost REQUIRED COMPONENTS serialization)


include_directories(${Boost_INCLUDE_DIRS})

find_package(SQLite3 REQUIRED)

add_executable(client_main mains/client_main.cc
               src/client.cc
               src/user.cc
               src/admin.cc
               src/connection.cc
               src/employee.cc
               src/room.cc
               src/hotel.cc)

add_executable(server_main mains/server_main.cc
              src/server.cc)

add_executable(employee_main mains/employee_main.cc
               src/client.cc
               src/user.cc
               src/admin.cc
               src/connection.cc
               src/employee.cc
               src/room.cc
               src/hotel.cc)

target_link_libraries(client_main ${Boost_LIBRARIES})
target_link_libraries(server_main ${Boost_LIBRARIES})
target_link_libraries(employee_main ${Boost_LIBRARIES})
target_link_libraries(client_main ${SQLite3_LIBRARIES})
target_link_libraries(server_main ${SQLite3_LIBRARIES})
target_link_libraries(employee_main ${SQLite3_LIBRARIES})