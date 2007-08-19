%define		_name		SnowIsh
Summary:	KDE Icons Theme - %{_name}
Summary(pl.UTF-8):	Motyw ikon dla KDE - %{_name}
Name:		kde-icons-%{_name}
Version:	1.3
Release:	1
License:	GPL
Group:		X11/Amusements
Source0:	http://pumphaus.kilu.de/files/%{_name}-kde-%{version}_build.tar.bz2
# Source0-md5:	6ca570cb19dce2615aca9843db53b7c0
URL:		http://www.kde-look.org/content/show.php?content=42905
BuildRequires:	ImageMagick
BuildRequires:	rpmbuild(macros) >= 1.123
BuildRequires:	tar
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE Icons Theme - %{_name}.

%description -l pl.UTF-8
Motyw ikon dla KDE - %{_name}.

%prep
%setup -q -n %{_name}-kde-%{version}_build
./buildset

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}

%{__tar} xfj %{_name}-%{version}.tar.bz2 -C $RPM_BUILD_ROOT%{_iconsdir}
mv $RPM_BUILD_ROOT%{_iconsdir}/%{_name}-%{version} $RPM_BUILD_ROOT%{_iconsdir}/%{_name}
install index.desktop $RPM_BUILD_ROOT%{_iconsdir}/%{_name}

rm -f `find $RPM_BUILD_ROOT -name .directory`

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%{_iconsdir}/%{_name}
