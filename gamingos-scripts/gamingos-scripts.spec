Name: gamingos-scripts
Version: 0.1.0
Release: 1%{?dist}
%define ver 43a0f458644648fab499dfd2035be7238e45999b
Summary: Scripts and services for a gaming OS
License: Apache-2.0
URL: https://github.com/LukeShortCloud/gamingos-scripts
Source0: https://github.com/LukeShortCloud/gamingos-scripts/archive/%{ver}.zip
BuildArch: noarch

%description
%{summary}.

%prep
%setup -q -c

%install
mkdir -p %{buildroot}/usr/lib/systemd/system/
cp -Rv gamingos-scripts-%{ver}/lib/systemd/system/* %{buildroot}/usr/lib/systemd/system/
mkdir -p %{buildroot}/usr/sbin/
cp -Rv gamingos-scripts-%{ver}/sbin/* %{buildroot}/usr/sbin/
mkdir -p %{buildroot}/usr/share/licenses/gamingos-scripts/
cp gamingos-scripts-%{ver}/LICENSE %{buildroot}/usr/share/licenses/gamingos-scripts/LICENSE

%files
/usr/lib/systemd/system/resize-root-file-system.service
/usr/sbin/resize-root-file-system.sh
/usr/share/licenses/gamingos-scripts/LICENSE

%post
/usr/bin/systemctl daemon-reload
# Manually enable the service for rpm-ostree distributions where systemd is not available during the build process.
ln -s /usr/lib/systemd/system/resize-root-file-system.service /etc/systemd/system/multi-user.target.wants/resize-root-file-system.service

%postun
rm -f /etc/systemd/system/multi-user.target.wants/resize-root-file-system.service
/usr/bin/systemctl daemon-reload

%changelog
* Tue May 23 2023 Luke Short <ekultails@gmail.com> 0.1.0
- Initial RPM spec created