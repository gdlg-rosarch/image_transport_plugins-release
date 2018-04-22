# Script generated with Bloom
pkgdesc="ROS - A set of plugins for publishing and subscribing to sensor_msgs/Image topics in representations other than raw pixel data. For example, for viewing a stream of images off-robot, a video codec will give much lower bandwidth and latency. For low frame rate tranport of high-definition images, you might prefer sending them as JPEG or PNG-compressed form."
url='http://www.ros.org/wiki/image_transport_plugins'

pkgname='ros-lunar-image-transport-plugins'
pkgver='1.9.5_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-lunar-catkin'
)

depends=('ros-lunar-compressed-depth-image-transport'
'ros-lunar-compressed-image-transport'
'ros-lunar-theora-image-transport'
)

conflicts=()
replaces=()

_dir=image_transport_plugins
source=()
md5sums=()

prepare() {
    cp -R $startdir/image_transport_plugins $srcdir/image_transport_plugins
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

