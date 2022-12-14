# ZeroMQ demo software

Quoted from [zeromq docs](https://zguide.zeromq.org/docs/preface/):

> ZeroMQ in a Hundred Words
>
> ZeroMQ (also known as ΓMQ, 0MQ, or zmq) looks like an embeddable networking library but acts like a concurrency framework.
> It gives you sockets that carry atomic messages across various transports like in-process, inter-process, TCP, and multicast.
> You can connect sockets N-to-N with patterns like fan-out, pub-sub, task distribution, and request-reply.
> Itβs fast enough to be the fabric for clustered products.
> Its asynchronous I/O model gives you scalable multicore applications, built as asynchronous message-processing tasks.
> It has a score of language APIs and runs on most operating systems.
> ZeroMQ is from iMatix and is LGPLv3 open source.

## Purpose of this particular directory

I was using `RabbitMQ` and `SocketIO` in my `python` and `JavaScript` projects already.
But then came `C++`.
I had trouble understanding the documentations and getting up and running in the `C++` environment.
The dependencies bummed me π
Eventually I found nice people from StackOverflow who shined the light on `ZeroMQ` π€©

Fortunately, the "hello world" examples were actually "readable" π€
Then, I followed the instructions, made some experiments, and as ZeroMQ puts it: ZAP! BOOM! POW! π₯
Things just worked out π

I'll put some demos here for "the future me" and anyone else interested πΆβπ«οΈ

## Building the first example

Follow the build instructions on [cppzmq](https://github.com/zeromq/cppzmq), in short:

1. Build [libzmq](https://github.com/zeromq/libzmq) following the usual `./configure`, `make`, and `sudo make install` procedure explained in `libzmq` [INSTALL](https://github.com/zeromq/libzmq/blob/master/INSTALL) file.
   Do this either by using your distro package manager, or building from source.

   ```bash
   # Create a top directory, we'll refer to this a few times during
   # the next steps
   TOPDIR="/path/to/top/directory"
   ```

2. Build and install [cppzmq](https://github.com/zeromq/cppzmq) via `CMake`:

   ```bash
   cd $TOPDIR
   git clone https://github.com/zeromq/cppzmq.git
   cd cppzmq
   mkdir build
   cd build
   cmake -DCMAKE_INSTALL_PREFIX=/usr/local ..
   sudo cmake --build . --target install
   ```

3. Build the `send` and `receive` programs from [hello world](hello-world):

   ```bash
   cd $TOPDIR
   git clone https://github.com/pedramardakani/serendipity.git
   cd serendipity/zeromq/hello-world
   mkdir build
   cmake ..
   make
   ```

4. Now open two terminals and run server and client on them, the order doesn't matter (cool, right?)

   ```bash
   # Run the server in terminal #1
   $TOPDIR/serendipity/zeromq/hello-wold/build/bin/server

   # Run the client in terminal #2
   $TOPDIR/serendipity/zeromq/hello-wold/build/bin/client
   ```

   Watch them exchanging messages!

## Building your own programs

   1. Set up the base project:

      ```bash
      # Set up the base project
      PDIR="/PATH/TO/YOUR/PROJECT"
      mkdir $PDIR && cd $PDIR

      # Copy the CMake instructions
      cp $TOPDIR/serendipity/zeromq/hello-world/CMakeLists.txt .

      # Create the file and finish your code
      touch main.cpp
      ```

   2. Update the `CMakeLists.txt` to contain your executable name.
      If you've named it `main.cpp` as shown above, change the following lines:

      ```txt
      # Change from this
      add_executable(
      client
      client.cpp
      )
      target_link_libraries(
      client
      PRIVATE cppzmq ${CMAKE_THREAD_LIBS_INIT}
      )

      # To this
      add_executable(
      main
      main.cpp
      )
      target_link_libraries(
      main
      PRIVATE cppzmq ${CMAKE_THREAD_LIBS_INIT}
      )
      ```

  3. The moment of truth.
     Create the build directory, build, and run your program:

     ```bash
     cd $PDIR
     mkdir build
     cmake ..
     make
     ./bin/main
     ```
