Summary:	Tux Typing - Graphical, educational typing tutorial game
Summary(pl):	Tux Typing - Gra edukacyjna, ucz�ca pisania na klawiaturze
Name:		tuxtype
Version:	1.0
Release:	2
License:	GPL
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(pl):	X11/Aplikacje/Gry
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-paths.patch
URL:		http://www.geekcomix.com/dm/tuxtype/
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_image-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Educational typing tutor starring Tux, the Linux Penguin. Object of
the game is to catch fish as they drop from the top of the screen.
Each fish has a letter or a word written on it, and Tux eats the fish
by the player pressing the associated key or typing the appropriate
word. Intended to be cute and fun for children learning to type and
spell.

%description -l pl
Nauka pisania z Tuksem, linuksowym pingwinem, w roli g��wnej. Celem
gry jest z�apanie rybek jak spadaj� z g�ry ekranu. Na ka�dej rybce
jest napisana litera, albo s�owo, a Tux zjada rybk� gdy gracz naci�nie
odpowiedni� klawisz, lub wpisze w�a�ciwe s�owo. Gra zosta�a pomy�lana
by by� mi�ym sposobem nauki pisania dla dzieci.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
automake -a
aclocal
autoconf
%configure
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Games

%{__make} install DESTDIR="$RPM_BUILD_ROOT"

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games/%{name}.desktop

gzip -9nf README AUTHORS TODO tuxtype/*/*.TXT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz tuxtype/*/*.TXT* tuxtype/docs/en/*.html
%attr(755,root,root) %{_bindir}/*
%{_datadir}/tuxtype
%{_applnkdir}/Games/*
