Name:           ros-kinetic-compressed-image-transport
Version:        1.9.4
Release:        0%{?dist}
Summary:        ROS compressed_image_transport package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/image_transport_plugins
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-cv-bridge
Requires:       ros-kinetic-dynamic-reconfigure
Requires:       ros-kinetic-image-transport
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-cv-bridge
BuildRequires:  ros-kinetic-dynamic-reconfigure
BuildRequires:  ros-kinetic-image-transport

%description
Compressed_image_transport provides a plugin to image_transport for
transparently sending images encoded as JPEG or PNG.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Sun Oct 02 2016 David Gossow <dgossow@willowgarage.com> - 1.9.4-0
- Autogenerated by Bloom

* Fri Apr 22 2016 David Gossow <dgossow@willowgarage.com> - 1.9.3-0
- Autogenerated by Bloom

