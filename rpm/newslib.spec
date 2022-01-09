Name:       newslib

Summary:    An almost completely useless example library
Version:    1
Release:    0
License:    LICENSE
URL:        http://example.org/
Source0:    %{name}-%{version}.tar.bz2
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
An almost completely useless example library

%package devel
Summary:    newslib development package
Requires:   %{name} = %{version}-%{release}

%description devel
Development files needed for using the newslib library

%prep
%setup -q -n %{name}-%{version}

%build
%qmake5 
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%qmake5_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libnews.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/news
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libnews.so

