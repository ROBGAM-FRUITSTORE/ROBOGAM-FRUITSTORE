#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/mgs09/tiago_public_ws/src/pal_navigation_sm"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/mgs09/tiago_public_ws/install/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/mgs09/tiago_public_ws/install/lib/python3/dist-packages:/home/mgs09/tiago_public_ws/build/pal_navigation_sm/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/mgs09/tiago_public_ws/build/pal_navigation_sm" \
    "/usr/bin/python3" \
    "/home/mgs09/tiago_public_ws/src/pal_navigation_sm/setup.py" \
     \
    build --build-base "/home/mgs09/tiago_public_ws/build/pal_navigation_sm" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/mgs09/tiago_public_ws/install" --install-scripts="/home/mgs09/tiago_public_ws/install/bin"
