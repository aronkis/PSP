CMAKE_MINIMUM_REQUIRED(VERSION 3.10)
project(ClientServer)

cmake_policy(SET CMP0167 NEW)
set(CMAKE_CXX_STANDARD 11)
find_package(Boost REQUIRED COMPONENTS serialization)


include_directories(${Boost_INCLUDE_DIRS})

find_package(SQLite3 REQUIRED)

add_executable(client_main client_main.cc
               src/client.cc
               src/clientS.cc)

add_executable(server_main server_main.cc
              src/server.cc)

target_link_libraries(client_main ${Boost_LIBRARIES})
target_link_libraries(server_main ${Boost_LIBRARIES})
target_link_libraries(client_main ${SQLite3_LIBRARIES})
target_link_libraries(server_main ${SQLite3_LIBRARIES})
